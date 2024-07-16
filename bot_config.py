from aiogram import Bot, Dispatcher
from os import getenv
from dotenv import load_dotenv
from database.database import Database
load_dotenv()

token = getenv("TOKEN")
bot = Bot(token=token)
dp = Dispatcher()
dp = Dispatcher()
db = Database("cafe.sqlite3")