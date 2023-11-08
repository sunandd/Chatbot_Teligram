from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import openai


class Reference:
    """
    a class to store previosly response from chatgpt api
    """

    def __init__(self) -> None:
        self.response =""


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

reference = Reference()
TOKEN = os.getenv("Token_teligram")

Model_name = "gpt-3.5-turbo"

#initialize bot and dispatcher

bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)


def clear_past():
    """
    forgeting previous contest
    """
    reference.response = ""

@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """
    This handler receives messages with `/start` command
    """
    await message.reply("Hi! \n welcome to Romio bot \n How may i assist you.") 

@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """
    This handler receives messages with `/clear` command
    """
    clear_past()
    await message.reply(" I have cleared message") 


@dispatcher.message_handler(commands=['help'])
async def help(message: types.Message):
    """
    This handler receives messages with '/help' command
    """

    help_command ="""
Thannk you for choseing us, please follow the command-\n /start - to start conversation.\n /clear - clearing previous conversation.\n /help - to get help menu.\nI hope this helps. """
    await message.reply(help_command) 
        

@dispatcher.message_handler()
async def chatgpt(message: types.Message):
    """
    A handler to process the user's input and generate a response using the chatGPT API.
    """
    print(f">>> USER: \n\t{message.text}")
    response = openai.ChatCompletion.create(
        model = Model_name,
        messages = [
            {"role": "assistant", "content": reference.response}, # role assistant
            {"role": "user", "content": message.text} #our query 
        ]
    )
    reference.response = response['choices'][0]['message']['content']
    print(f">>> chatGPT: \n\t{reference.response}")
    await bot.send_message(chat_id = message.chat.id, text = reference.response)



if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=True) 


