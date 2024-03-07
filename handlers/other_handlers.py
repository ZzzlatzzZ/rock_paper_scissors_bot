from aiogram import Router
from aiogram.types import Message
from lexicons.lexicon_ru import LEXICON_RU

# Инициализируем роутер
router = Router()

# Хэндлер для всех сообщений
@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])