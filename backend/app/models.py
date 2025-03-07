from sqlalchemy import Column, Integer, String

from app.database import Base, engine


class UserDBModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    token = Column(String, nullable=True)


Base.metadata.create_all(bind=engine)
