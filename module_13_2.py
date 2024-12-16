import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async  def start_message(message: Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')