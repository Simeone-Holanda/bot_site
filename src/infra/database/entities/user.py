from pydantic import BaseModel, validator
from typing import int, Optional
from random import randrange

class UserAuth(BaseModel):
    """ Modelo de dados do User"""
    id : Optional[str]
    email : str
    code : int

    @classmethod
    def generate_code(cls):
        """ Gerador de codigo"""
        return randrange(999999+1)


    