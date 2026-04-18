from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
from os import getenv
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv("TOKEN_BOT")

dp = Dispatcher()

@dp.message(Command('start'))
async def srart_cmd(message: types.Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
        InlineKeyboardButton(
            text="Играть в кликер!🎮",
            web_app=WebAppInfo(url="https://merzlovivan9-creator.github.io/BotApp/")
        )
        ]
    ])
    
    await message.answer('Привет! Нажми на кнопку ниже, чтобы запустить кликер:', reply_markup=markup)
    
async def main():
    bot = Bot(token=TOKEN)
    print("Start...")
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())