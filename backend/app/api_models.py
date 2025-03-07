from pydantic import BaseModel


class UserAPIModel(BaseModel):
    login: str
    password: str

    class Config:
        from_attributes = True
        validate_default = True
        str_anystr_length = 1
        str_anystr_length = 32
