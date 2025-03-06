from sqlalchemy import Column, Integer, String
from pydantic import BaseModel

from app.database import Base, engine


class UserDBModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    token = Column(String, nullable=True)


class UserAPIModel(BaseModel):
    login: str
    password: str

    class Config:
        from_attributes = True
        validate_default = True
        str_anystr_length = 1
        str_anystr_length = 32


Base.metadata.create_all(bind=engine)
