from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
import jwt
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

ACCESS_TOKEN_EXPIRE_TIME = 5  # in minutes
SECRET_KEY = os.environ["SECRET_KEY"]
ALGORITHM = "HS256"


async def is_token_valid(token: str) -> bool:
    """
    Check the validity of a JWT token.

    :param token: JSON Web Token (JWT) string to be validated.
    :type token: str
    :return: A boolean indicating whether the token is valid.
    :rtype: bool
    """
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
    """
    Generates a JWT token for user authentication.

    :param login: Login of the user.
    :type login: str
    :param password: The password credential of the user.
    :type password: str
    :return: A JWT token string representing the encoded user credentials
        and expiration timestamp.
    :rtype: str
    """
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_TIME)
    to_encode = {"login": login,
                 "password": password,
                 "expire": expire.timestamp()}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
