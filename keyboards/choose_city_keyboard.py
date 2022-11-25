from aiogram import types


choose_moscow_button = types.InlineKeyboardButton('Москва', callback_data='moskva')
choose_podolsk_button = types.InlineKeyboardButton('Подольск', callback_data='podolsk')

choose_city_keyboard = types.InlineKeyboardMarkup()
choose_city_keyboard.add(choose_moscow_button).add(choose_podolsk_button)
