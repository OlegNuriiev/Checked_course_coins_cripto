
from telebot.async_telebot import AsyncTeleBot

import requests
import asyncio

bot =AsyncTeleBot('')

@bot.message_handler(commands=['start'])
async def stars_message(message):
    await bot.send_message(message.chat.id, """
    Привет! С помощью этого бота сможешь мониторить курс криптовалют
    """)
