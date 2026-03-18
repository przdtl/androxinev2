from fastapi import status

from presentation.api.responses.auth import UNAUTHORIZED_RESPONSE
from presentation.api.schemas.common import APIError, ErrorResponse


LIST_CATEGORY_RESPONSES = {}

LIST_CATEGORY_RESPONSES.update(UNAUTHORIZED_RESPONSE)
