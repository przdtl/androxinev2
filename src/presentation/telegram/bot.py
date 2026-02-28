import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Update

from config import settings
from db.base import async_session_maker
from uow import UnitOfWork
from presentation.telegram.middlewares import UOWMiddleware

logger = logging.getLogger(__name__)


bot = Bot(
    token=settings.TELEGRAM_BOT_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML,
    ),
)
dp = Dispatcher()

dp.message.middleware(UOWMiddleware())


async def setup_webhook():
    """Устанавливает webhook для бота"""
    if settings.TELEGRAM_WEBHOOK_URL:
        webhook_url = settings.TELEGRAM_WEBHOOK_URL
        logger.info(f"Устанавливаем webhook: {webhook_url}")
        await bot.set_webhook(
            url=webhook_url,
            drop_pending_updates=True,
        )
        logger.info("Webhook установлен успешно")
    else:
        logger.warning("TELEGRAM_WEBHOOK_URL не установлен, webhook не будет настроен")


async def shutdown_webhook():
    """Удаляет webhook при остановке"""
    logger.info("Удаляем webhook...")
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.session.close()
    logger.info("Webhook удален")


async def get_uow() -> UnitOfWork:
    """Factory для создания UnitOfWork для handlers"""
    async with async_session_maker() as session:
        async with UnitOfWork(session) as uow:
            return uow


async def process_update(update: dict):
    """Обрабатывает входящий update от Telegram"""
    logger.info(f"Получен update: {update}")
    telegram_update = Update(**update)
    dp["get_uow"] = get_uow
    await dp.feed_update(bot=bot, update=telegram_update)
    logger.info("Update обработан успешно")
