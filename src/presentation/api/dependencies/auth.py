import jwt

from typing import Annotated

from fastapi import Depends

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from services.jwt import JWTService

from config import settings

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> int:
    jwt_service = JWTService(secret_key=settings.JWT_SECRET_KEY)
    try:
        payload = jwt_service.decode(credentials.credentials)
    except jwt.InvalidTokenError:
        raise HTTPBearer().make_not_authenticated_error()

    return int(payload.sub)


UserDep = Annotated[int, Depends(get_current_user)]
