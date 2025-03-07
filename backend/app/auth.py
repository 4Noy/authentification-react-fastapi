from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
import jwt
import os

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
