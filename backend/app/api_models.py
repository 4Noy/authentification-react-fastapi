from pydantic import BaseModel


class UserAPIModel(BaseModel):
    """
    Represents a user model for API interactions.

    :ivar login: User login.
    :type login: str
    :ivar password: User password.
    :type password: str
    """
    login: str
    password: str

    class Config:
        from_attributes = True
        validate_default = True
        str_anystr_length = 1
        str_anystr_length = 32


class TokenVerificationAPIModel(BaseModel):
    """
    Represents a data model for token verification in an API.

    :ivar login: User login.
    :type login: str
    :ivar token: Authentication token.
    :type token: str
    """
    login: str
    token: str

    class Config:
        from_attributes = True
        validate_default = True
        str_anystr_length = 1
        str_anystr_length = 32
