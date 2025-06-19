from fastapi import APIRouter
from jwt_manager import create_token
from fastapi.responses import JSONResponse
from schema.user import User

user_router = APIRouter()

@user_router.post('/login', tags=['Login'])
def login(user:User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code = 200, content = {"token": token})
    
