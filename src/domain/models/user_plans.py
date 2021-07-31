from typing import Union
from pydantic.main import BaseModel 
from .permissions import Level_1, Level_2, Level_3, Level_4


class UserPlans(BaseModel):
    config: Union[Level_1, Level_2, Level_3, Level_4]
