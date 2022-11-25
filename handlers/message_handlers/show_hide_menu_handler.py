from aiogram import types

from loader import dp, bot
from keyboards import main_menu_keyboard


@dp.message_handler(commands=['hide_menu'])
async def show_hide_menu(message: types.Message):
    await bot.send_message(message.chat.id, 'Меню скрыто', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands=['show_menu'])
async def show_hide_menu(message: types.Message):
    await bot.send_message(message.chat.id, 'Меню активно', reply_markup=main_menu_keyboard)
