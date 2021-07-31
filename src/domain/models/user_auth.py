from typing import Optional
from pydantic.main import BaseModel
from pydantic.networks import EmailStr
from pydantic.types import conint
from pydantic.class_validators import validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError


class UserAuth(BaseModel):
    id: Optional[str]
    email: EmailStr
    code: conint(ge=0, lt=1000000)

    @validator('code', pre=True)
    def validate_code(cls, v):
        if(isinstance(v,bool)):
            raise ValidationError([ErrorWrapper(Exception('ensure this value is not type of boolean'), loc="must not be type of bool")],
            model=UserAuth,)
        return v
