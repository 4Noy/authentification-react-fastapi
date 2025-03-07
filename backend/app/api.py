from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.api_models import UserAPIModel, TokenVerificationAPIModel
from app.auth import is_token_valid, generate_token
from app.models import UserDBModel
from app.database import get_db

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Line edited by AI
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root() -> dict:
    """
    Base endpoint for testing the connection.

    :return: A dictionary containing a confirmation message.
    :rtype: dict
    """
    return {"message": "Connection Established to FastAPI !"}


@app.get("/users")
async def get_users(db: Session = Depends(get_db)) -> dict:
    """
    Retrieves a list of all user logins from the database.

    :param db: The database session.
    :type db: Session

    :return: A dictionary containing a list of user logins under the
             key `"users"`.
    :rtype: dict
    """
    return {"users":
            [user_login[0] for user_login in
             db.query(UserDBModel.login).all()]}


@app.post("/create_user")
async def create_user(newuser: UserAPIModel,
                      db: Session = Depends(get_db)) -> dict:
    """
    Creates a new user in the database if the provided login and password meet the
    necessary conditions.

    :param newuser: An instance of UserAPIModel.
    :type newuser: UserAPIModel

    :param db: The database session.
    :type db: Session

    :return: A dictionary containing a confirmation message when the user is
        successfully created.
    :rtype: dict
    """
    if (db.query(UserDBModel.login).filter(UserDBModel.login == newuser.login).first() != None):
        raise HTTPException(status_code=409, detail="User Already Exists")
    if (len(newuser.password) != 64):
        raise HTTPException(status_code=400, detail="Password hash incorrect")

    try:
        newusermodel = UserDBModel(**newuser.dict())
        db.add(newusermodel)
        db.commit()
        return {"message": "New User Created."}
    except Exception:
        raise HTTPException(status_code=500, detail="Couln't add new user")


@app.post("/connect")
async def connect(user: UserAPIModel,
                  db: Session = Depends(get_db)) -> dict:
    """
    Handle user connection.

    :param user: The user credentials for authentication.
    :type user: UserAPIModel
    :param db: The database session dependency.
    :type db: Session

    :return: Dictionary containing a success message and the generated token.
    :rtype: dict
    """
    connecteduser: UserDBModel or None = db.query(UserDBModel)\
            .where(UserDBModel.login == user.login).first()
    if (connecteduser is None):
        raise HTTPException(status_code=404, detail="User doesn't exist")
    if (connecteduser.password != user.password):
        raise HTTPException(status_code=401, detail="Wrong Password !")
    token = await generate_token(user.login, user.password)
    try:
        connecteduser.token = token
        db.commit()
    except Exception:
        raise HTTPException(status_code=500, detail="Couldn't connect")

    return {"message": "Connected", "token": token}


@app.post("/verify_token")
async def verify_token(tokenAndLogin: TokenVerificationAPIModel,
                       db: Session = Depends(get_db)) -> dict:
    """
    Verifies the authenticity of a user token.

    :param tokenAndLogin: The object containing user login and their associated
        token.
    :type tokenAndLogin: TokenVerificationAPIModel
    :param db: The database session dependency.
    :type db: Session

    :return: A dictionary confirming verification of the token with
        a success message.
    :rtype: dict
    """
    user_login = tokenAndLogin.login
    token = tokenAndLogin.token
    connecteduser: UserDBModel or None = db.query(UserDBModel)\
            .where(UserDBModel.login == user_login).first()
    if (connecteduser is None):
        raise HTTPException(status_code=404, detail="User doesn't exist")
    if (connecteduser.token == token and await is_token_valid(token)):
        return {"message": "Token Verified"}
    else:
        raise HTTPException(status_code=401, detail="Invalid Token")
