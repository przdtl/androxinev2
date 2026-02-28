import re

from dataclasses import dataclass

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from uow import UnitOfWork
from dto.sets.create_by_short import CreateSetByExerciseShortInputDTO
from use_cases.sets.create_from_bot import CreateSetFromBotUseCase


router = Router()


@dataclass
class SetParseResult:
    short: str
    weight: float
    reps: int


def parse_add_command(text: str) -> SetParseResult | None:
    """
    Парсит команду добавления подхода.
    Поддерживает форматы:
    - /add <short> <вес> <повторения>
    - /add <short> <вес>x<повторения>

    Возвращает: (short, вес, повторения) или None если не удалось распарсить
    """
    text = text.strip()
    if text.startswith("/add"):
        text = text[4:].strip()

    # формат: short вес x повторения
    pattern1 = r"^(\S+)\s+(\d+\.?\d*)\s*x\s*(\d+)$"
    match = re.match(pattern1, text, re.IGNORECASE)
    if match:
        short, weight, reps = match.groups()
        return SetParseResult(
            short=short,
            weight=float(weight),
            reps=int(reps),
        )

    # формат: short вес повторения
    pattern2 = r"^(\S+)\s+(\d+\.?\d*)\s+(\d+)$"
    match = re.match(pattern2, text)
    if match:
        short, weight, reps = match.groups()
        return SetParseResult(
            short=short,
            weight=float(weight),
            reps=int(reps),
        )

    return None


@router.message(Command("add"))
async def add_set_handler(message: Message, uow: UnitOfWork):
    """
    Обработчик команды /add для добавления подхода.

    Примеры использования:
    /add bench 100 10
    /add squat 120 8
    /add bench 100x10
    /add squat 120x8
    """
    if not message.text:
        await message.answer(
            "❌ Неверный формат команды.\n\n"
            "Используйте:\n"
            "/add <упражнение> <вес> <повторения>\n"
            "или\n"
            "/add <упражнение> <вес>x<повторения>\n\n"
            "Примеры:\n"
            "/add bench 100 10\n"
            "/add squat 120x8"
        )
        return

    parsed = parse_add_command(message.text)
    if not parsed:
        await message.answer(
            "❌ Не удалось распознать команду.\n\n"
            "Используйте:\n"
            "/add <упражнение> <вес> <повторения>\n"
            "или\n"
            "/add <упражнение> <вес>x<повторения>\n\n"
            "Примеры:\n"
            "/add bench 100 10\n"
            "/add squat 120x8"
        )
        return

    if not message.from_user:
        await message.answer("❌ Не удалось определить пользователя.")
        return

    print(f"Дата команды: {message.date}")

    use_case = CreateSetFromBotUseCase(uow)
    dto = CreateSetByExerciseShortInputDTO(
        user_id=message.from_user.id,
        exercise_short=parsed.short,
        weight=parsed.weight,
        reps=parsed.reps,
        created_at=message.date,
    )

    result = await use_case.execute(dto)

    if not result:
        await message.answer(
            f"❌ Упражнение с кодом '{parsed.short}' не найдено.\n\n"
            f"Проверьте код упражнения и попробуйте снова."
        )
        return

    await message.answer(
        f"✅ Подход добавлен!\n\n"
        f"🏋️ {result.exercise_title}\n"
        f"⚖️ Вес: {result.weight} кг\n"
        f"🔁 Повторения: {result.reps}\n"
        f"📅 {result.created_at.strftime('%d.%m.%Y %H:%M')}"
    )
