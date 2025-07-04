from fastapi import FastAPI, Request, HTTPException
#from fastapi.responses import JSONResponse
#from pydantic import BaseModel
from jwt_manager import validate_token
from fastapi.security import HTTPBearer
from config.database import  engine, Base
from middlewares.error_handler import ErrorHandler
from routers.book import book_router
from routers.user import user_router
#json response investigacion

app = FastAPI()
app.title = "Lo quiero mucho profe, ojalá el aoty sea de sincerely"
app.version = "0.0.1"

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Para desarrollo, luego puedes poner solo tu IP pública
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_middleware(ErrorHandler)
app.include_router(book_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Credenciales no validas")





#ORM y sqlalchemy

