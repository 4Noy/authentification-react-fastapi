from sqlalchemy import Column, Integer, String

from app.database import Base, engine


class UserDBModel(Base):
    """
    Represents a database model for users.

    :ivar id: Serial, Primary Key
    :type id: int
    :ivar login: Unique login.
    :type login: str
    :ivar password: Hashed Password.
    :type password: str
    :ivar token: Optional authentication token.
    :type token: str or None
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    token = Column(String, nullable=True)


Base.metadata.create_all(bind=engine)
