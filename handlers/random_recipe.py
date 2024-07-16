from bot_config import bot,dp
from aiogram import types,Router,F
from aiogram.filters import Command
import random

recipe_router= Router()
recipes = [['manty',['meat','dough']],
           ['plov',['meat','rice','carrot']],
           ['kuurdak',['meat','potato']]]

@recipe_router.message(Command("random_recipe"))
async def random_recipe(message:types.Message):
    random_recipe = random.choice(recipes)
    await message.answer(f'{random_recipe[0]}\n'
                         f'{random_recipe[1]}')