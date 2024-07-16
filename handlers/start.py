from bot_config import bot,dp
from aiogram import types,Router,F
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command("start"))
async def start(message:types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='О нас', callback_data='about_us'),
                types.InlineKeyboardButton(text='Наш инстаграм', url='https://instagram.com')
            ],
            [
                types.InlineKeyboardButton(text='Наш адрес', url='https://2gis.kg'),
                types.InlineKeyboardButton(text='Вакансии', callback_data='jobs')
            ],
            [
                types.InlineKeyboardButton(text='Оставить отзыв', callback_data="feedback")
            ]
        ]
    )

    await message.answer(f"Hi {message.from_user.first_name}",reply_markup=kb)
@start_router.callback_query(F.data=="about_us")
async def about_us(message:types.Message):
    await message.answer("nothing yet")

@start_router.callback_query(F.data=='review')
async def review(message: types.Message):
    await message.answer('nothing yet')

@start_router.callback_query(F.data=='jobs')
async def jobs(message:types.Message):
    await message.answer("nothing yet")