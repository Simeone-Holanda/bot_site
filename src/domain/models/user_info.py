from typing import Optional
from pydantic.main import BaseModel
from pydantic.class_validators import validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from datetime import date, timedelta
import re

class UserInfo(BaseModel):
    user_id: Optional[str]
    cpf: str
    born_at: date
    agree: bool

    @validator('cpf')
    def validate_cpf(cls, v):
        if re.compile('^([0-9]{3}[\.][0-9]{3}[\.][0-9]{3}[-][0-9]{2})$').search(v):
            return v
        raise ValidationError([ErrorWrapper(Exception('ensure this value on cpf format'), loc="must be on format of cpf")],
        model=UserInfo,)
    @validator('born_at')
    def validate_born_at(cls, v):
        if v>date.today()-timedelta(days=365*100) and v<(date.today()-timedelta(days=365*18)):
            return v
        raise ValidationError([ErrorWrapper(Exception('ensure you have more than 18 years and less than 100'), loc="must have right age")],
        model=UserInfo,)
