from fastapi import APIRouter, Request, Response

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
