from typing import Optional
from pydantic.main import BaseModel

class Account(BaseModel):
    user_id: Optional[str]
    name: str
    validated: bool
