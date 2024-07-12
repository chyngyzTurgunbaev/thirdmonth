from bot_config import bot, dp
from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

review_router = Router()


class RestarauntReview(StatesGroup):
    name = State()
    instagram_username = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()


@review_router.callback_query(F.data == "feedback")
async def feedback_callback(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(RestarauntReview.name)
    await call.message.answer("Ваше имя")


@review_router.message(RestarauntReview.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.set_state(RestarauntReview.instagram_username)
    await message.answer("Ваш инстаграм аккаунт")


@review_router.message(RestarauntReview.instagram_username)
async def process_instagram(message: types.Message, state: FSMContext):
    await state.set_state(RestarauntReview.visit_date)
    await message.answer("Дата визита")


@review_router.message(RestarauntReview.visit_date)
async def process_visit_date(message: types.Message, state: FSMContext):
    await state.set_state(RestarauntReview.food_rating)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Плохо")],
            [types.KeyboardButton(text="Удовлетворительно")]
        ]
    )
    await message.answer("Оценка еды", reply_markup=kb)


@review_router.message(RestarauntReview.food_rating)
async def process_food_rating(message: types.Message, state: FSMContext):
    await state.set_state(RestarauntReview.cleanliness_rating)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Плохо")],
            [types.KeyboardButton(text="Удовлетворительно")]
        ]
    )

    await message.answer("Оценка чистоты", reply_markup=kb)


@review_router.message(RestarauntReview.cleanliness_rating)
async def process_cleanliness_rating(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardRemove()
    await state.set_state(RestarauntReview.extra_comments)
    await message.answer("Дополнительные комментарии", reply_markup=kb)


@review_router.message(RestarauntReview.extra_comments)
async def process_extra_comments(message: types.Message, state: FSMContext):
    await message.answer("Отзыв оставлен")
    await state.clear()
