from fastapi import APIRouter, Request, Response

from config import settings
from presentation.telegram import process_update

router = APIRouter(prefix="/webhook", tags=["Telegram Webhook"])


@router.post("/telegram")
async def telegram_webhook(request: Request):
    """
    Endpoint для получения обновлений от Telegram через webhook.
    Telegram будет отправлять сюда POST запросы с обновлениями.
    """
    update = await request.json()
    await process_update(update)
    return Response(status_code=200)


@router.get("/telegram")
async def telegram_webhook_info():
    """
    Информация о webhook (для проверки)
    """
    return {
        "webhook_path": settings.TELEGRAM_WEBHOOK_PATH,
        "webhook_url": settings.TELEGRAM_WEBHOOK_URL,
        "status": "active" if settings.TELEGRAM_WEBHOOK_URL else "not configured",
    }
