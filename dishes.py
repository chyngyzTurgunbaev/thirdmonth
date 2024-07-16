from bot_config import bot,dp
from aiogram import types,Router,F
from aiogram.filters import Command
import random


dishes_router = Router()

@dishes_router.message(F.text=="напитки")
async def drinks(message:types.Message):
    await message.answer("")