from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import openai


class Referance:
    """
    a class to store previosly response from chatgpt api
    """

    def __init__(self) -> None:
        self.responce =""


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

referance = Referance()
TOKEN = os.getenv("Token_teligram")

Model_name = "gpt-3.5-turbo"

#initialize bot and dispatcher

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



