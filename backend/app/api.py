from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from app.user import UserDBModel, UserAPIModel
from app.database import get_db

app = FastAPI()


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
                  token: str,
                  db: Session = Depends(get_db)) -> dict:
    connecteduser: UserDBModel or None = db.query(UserDBModel)\
            .where(UserDBModel.login == user.login).first()
    if (connecteduser is None):
        raise HTTPException(status_code=404, detail="User doesn't exist")
    if (connecteduser.password != user.password):
        raise HTTPException(status_code=401, detail="Wrong Password !")
    return {"message": "Connected"}
