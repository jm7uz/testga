"""
This is a echo bot.
It echoes any incoming text messages.
"""


import aiohttp
import asyncio
import logging
import requests
from aiogram import Bot, Dispatcher, executor, types

def saverapi(url):
    headers = {'content-type' : 'application/json', 
        'referer':'https://save-from.net/', 
        'Origin': 'https://save-from.net',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    data ={"url":url}
    url = ("https://save-from.net/api/convert")
    r = requests.post(url, params=data, headers=headers)
    try:
        r = r.json()
        id = r['id'] if 'id' in r else None
        manzil = r['url'] if 'url' in r else None
        info = r['meta'] if 'meta' in r else None
        return manzil
    except Exception as e:
        print(e)




API_TOKEN = '5523450306:AAHOdqmLf_O6Hspc_ttOsJmcw3lY-FxUUc4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/cats.jpg', 'rb') as photo:
        '''
        # Old fashioned way:
        await bot.send_photo(
            message.chat.id,
            photo,
            caption='Cats are here 😺',
            reply_to_message_id=message.message_id,
        )
        '''

        await message.reply_photo(photo, caption='Cats are here 😺')


@dp.message_handler()
async def echo(message: types.Message):
    urls = saverapi(url=message.text)
    print(urls[0]['url'])
    try:
        await bot.send_video(chat_id=message.from_user.id,
                            video=urls)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)