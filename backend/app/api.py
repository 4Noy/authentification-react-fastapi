from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import logging

from app.user import UserDBModel, UserAPIModel
from app.database import get_db

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Connection Established to FastAPI !"}


@app.get("/users")
async def get_users(db: Session = Depends(get_db)):
    return {"users":
            [user_login[0] for user_login in
             db.query(UserDBModel.login).all()]}


@app.post("/create_user")
async def create_user(newuser: UserAPIModel, db: Session = Depends(get_db)):
    if (any(newuser.login == user_login
            for user_login in db.query(UserDBModel.login))):
        raise HTTPException(status_code=409, detail="User Already Exists")

    try:
        newusermodel = UserDBModel(**newuser.dict())
        db.add(newusermodel)
        db.commit()
    except Exception:
        logging.warning("Couldn't add new user: " + newuser.login)
