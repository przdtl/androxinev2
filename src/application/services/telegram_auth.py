import hashlib
import hmac
from urllib.parse import parse_qsl


class TelegramAuthService:
    def __init__(self, bot_token: str):
        self._bot_token = bot_token

    def validate_init_data(self, init_data: str) -> dict[str, str] | None:
        """
        Validates Telegram WebApp init_data.

        Returns parsed data dict if valid, None if invalid.

        See: https://core.telegram.org/bots/webapps#validating-data-received-via-the-mini-app
        """
        try:
            parsed_data = dict(parse_qsl(init_data))

            if "hash" not in parsed_data:
                return None

            received_hash = parsed_data.pop("hash")

            # Create data check string
            data_check_arr = [f"{k}={v}" for k, v in sorted(parsed_data.items())]
            data_check_string = "\n".join(data_check_arr)

            # Calculate secret key
            secret_key = hmac.new(
                key=b"WebAppData",
                msg=self._bot_token.encode(),
                digestmod=hashlib.sha256,
            ).digest()

            # Calculate hash
            calculated_hash = hmac.new(
                key=secret_key,
                msg=data_check_string.encode(),
                digestmod=hashlib.sha256,
            ).hexdigest()

            if calculated_hash != received_hash:
                return None

            return parsed_data

        except Exception:
            return None

    def extract_user_id(self, validated_data: dict[str, str]) -> int | None:
        """Extract user.id from validated init_data."""
        try:
            import json

            user_data = json.loads(validated_data.get("user", "{}"))
            return user_data.get("id")
        except Exception:
            return None
