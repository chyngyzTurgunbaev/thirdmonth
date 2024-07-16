from bot_config import bot,dp
from aiogram import types,Router,F
from aiogram.filters import Command

my_info_router = Router()


@my_info_router.message(Command("myinfo"))
async def my_info(message:types.Message):
    await message.answer(f"Name: {message.from_user.first_name}\n"
                         f"id: {message.from_user.id}")