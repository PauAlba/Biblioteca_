from pydantic import BaseModel
from fastapi import APIRouter, Depends

class User(BaseModel):
    email:str
    password:str