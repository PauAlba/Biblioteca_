from jwt import encode, decode
#from fastapi.security import HTTPBearer
#from fastapi import Request, HTTPException
#from jwt_manager import validate_token

def create_token(data:dict):
  token: str = encode(payload=data, key="my_secret_key", algorithm="HS256")
  return token

def validate_token(token: str):
  data : dict = decode(token, key="my_secret_key", algorithms=["HS256"])
  return data