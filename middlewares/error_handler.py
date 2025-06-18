from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException

class ErrorHandler(BaseHTTPMiddleware):
  def __init__(self, app: FastAPI) -> None:
    super().__init__(app)

  async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
    try:
      return await call_next(request)
    except Exception as e:
      return JSONResponse(status_code=500, content={"error": str(e)})
    
class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            # Aquí validas el token
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid token")