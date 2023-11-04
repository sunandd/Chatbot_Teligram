import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv("Token_teligram")


#configure logging
logging .basicConfig(level=logging.INFO)

#initialize bot
bot= Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start',  'help'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` command
    """
    await message.reply("Hi! \n i am telibot \n powered by open ai.")

@dp.message_handler()
async def echo(message: types.Message):
    """
    echo  every message
    """
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True) 
