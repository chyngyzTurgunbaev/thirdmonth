from bot_config import bot,dp
import asyncio
from handlers.random_recipe import recipe_router
from handlers.start import start_router
from handlers.my_info import my_info_router
from handlers.review_dialog import review_router
from bot_config import db
async def main():
    db.create_tables()
    dp.include_router(start_router)
    dp.include_router(recipe_router)
    dp.include_router(my_info_router)
    dp.include_router(review_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())