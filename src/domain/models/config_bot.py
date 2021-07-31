from typing import Optional, List
from pydantic.main import BaseModel
from pydantic.fields import Field
from permissions import Permissions

class ConfigBot(BaseModel):
    account_id: Optional[str]
    name: str= Field(...,min_length=4, max_length=21)
    actions: List[Permissions.Enumerate]
    validated: bool
