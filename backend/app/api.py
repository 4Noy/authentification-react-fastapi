import os
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
import jwt
from sqlalchemy.orm import Session

from app.user import UserDBModel, UserAPIModel
from app.database import get_db

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

ACCESS_TOKEN_EXPIRE_TIME = 5  # in minutes
SECRET_KEY = os.environ["SECRET_KEY"]
ALGORITHM = "HS256"


async def is_token_valid(token: str) -> bool:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if datetime.utcnow() > datetime.fromtimestamp(payload["expire"]):
            return False
        return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False


async def generate_token(login: str, password: str) -> str:
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_TIME)
    to_encode = {"login": login,
                 "password": password,
                 "expire": expire.timestamp()}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


@app.get("/")
async def read_root() -> dict:
    return {"message": "Connection Established to FastAPI !"}


@app.get("/users")
async def get_users(db: Session = Depends(get_db)) -> dict:
    return {"users":
            [user_login[0] for user_login in
             db.query(UserDBModel.login).all()]}


@app.post("/create_user")
async def create_user(newuser: UserAPIModel,
                      db: Session = Depends(get_db)) -> dict:
    if (any(newuser.login == user_login
            for user_login in db.query(UserDBModel.login))):
        raise HTTPException(status_code=409, detail="User Already Exists")

    try:
        newusermodel = UserDBModel(**newuser.dict())
        db.add(newusermodel)
        db.commit()
        return {"message": "New User Created"}
    except Exception:
        raise HTTPException(status_code=500, detail="Couln't add new user")


@app.post("/connect")
async def connect(user: UserAPIModel,
                  db: Session = Depends(get_db)) -> dict:
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
async def verify_token(user_login: str,
                       token: str,
                       db: Session = Depends(get_db)) -> dict:
    connecteduser: UserDBModel or None = db.query(UserDBModel)\
            .where(UserDBModel.login == user_login).first()
    if (connecteduser is None):
        raise HTTPException(status_code=404, detail="User doesn't exist")
    if (connecteduser.token == token and is_token_valid(token)):
        return {"message": "Token Verified"}
    else:
        raise HTTPException(status_code=401, detail="Invalid Token")
