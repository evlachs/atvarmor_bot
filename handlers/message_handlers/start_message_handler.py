from aiogram import types

from loader import dp, bot

from messages import MESSAGES
from keyboards import main_menu_keyboard


@dp.message_handler(commands=['start'])
async def send_welcome_message(message: types.Message):
    await bot.send_message(message.chat.id, MESSAGES['welcome_message'], reply_markup=main_menu_keyboard)
