from aiogram import Bot, Dispatcher,types
from aiogram.filters import Command
import asyncio
from os import getenv
from dotenv import load_dotenv
import random
load_dotenv()

token = getenv("TOKEN")
bot = Bot(token=token)
dp = Dispatcher()
recipes = [['manty',['meat','dough']],
           ['plov',['meat','rice','carrot']],
           ['kuurdak',['meat','potato']]]
@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer(f"Hi {message.from_user.first_name}")

@dp.message(Command("my_info"))
async def my_info(message:types.Message):
    await message.answer(f"Name: {message.from_user.first_name}\n"
                         f"id: {message.from_user.id}")

@dp.message(Command("random_recipe"))
async def random_recipe(message:types.Message):
    random_recipe = random.choice(recipes)
    await message.answer(f'{random_recipe[0]}\n'
                         f'{random_recipe[1]}')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())