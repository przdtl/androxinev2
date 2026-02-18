import jwt
import datetime

from typing import Any

from dto.auth import PayloadDTO, PayloadDataDTO


class JWTService:
    def __init__(
        self,
        secret_key: str,
        algorithm: str = "HS256",
        access_token_expire_minutes: int = 60 * 24,
    ):
        self._secret_key = secret_key
        self._algorithm = algorithm
        self._access_token_expire_minutes = access_token_expire_minutes

    def create_access_token(
        self,
        data: PayloadDataDTO,
    ) -> str:
        now = datetime.datetime.now(datetime.UTC)
        payload = PayloadDTO(
            sub=data.telegram_id,
            iat=int(now.timestamp()),
            exp=int(
                (
                    now + datetime.timedelta(minutes=self._access_token_expire_minutes)
                ).timestamp()
            ),
        )

        encoded_jwt = jwt.encode(
            payload=payload.model_dump(),
            key=self._secret_key,
            algorithm=self._algorithm,
        )
        return encoded_jwt

    def decode_token(self, token: str) -> dict[str, Any] | None:
        """Decode and validate JWT token."""
        try:
            payload = jwt.decode(
                jwt=token,
                key=self._secret_key,
                algorithms=[self._algorithm],
            )
            return payload
        except jwt.PyJWTError:
            return None
