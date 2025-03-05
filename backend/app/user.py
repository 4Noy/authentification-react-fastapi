from database import Base
from sqlalchemy import Column, Integer, String, Text
import bcrypt


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    login = Column(String, nullable=False)
    password = Column(Text, nullable=False)

    def verify_password(self, password):
        pswhash = bcrypt.hashpw(password, self.password)
        return self.password == pswhash
