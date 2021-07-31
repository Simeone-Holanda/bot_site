from typing import Optional, Literal, List
from pydantic import BaseSettings
from enum import Enum


class Permissions:
    class Enumerate(str, Enum):
        arena='arena'
        get_gold='ggd'
        donate_silver='dsv'
        donate_gold='dgd'
        torneio_imortals='timortals'
        torneio_clans='tclans'
        events='evt'
    options=[i.value for i in Enumerate]
    level_1=options[:2]
    level_2=options[:4]
    level_3=options[:6]
    level_4=options

class Level_1(BaseSettings):
    type: Literal['bronze']
    account_id: Optional[str]
    permissions: List[Permissions.Enumerate]=Permissions.level_1

class Level_2(BaseSettings):
    type: Literal['silver']
    account_id: Optional[str]
    permissions: List[Permissions.Enumerate]=Permissions.level_2

class Level_3(BaseSettings):
    type: Literal['gold']
    account_id: Optional[str]
    permissions: List[Permissions.Enumerate]=Permissions.level_3

class Level_4(BaseSettings):
    type: Literal['diamond']
    account_id: Optional[str]
    permissions: List[Permissions.Enumerate]=Permissions.level_4