from aiogram import types


atv_button = types.InlineKeyboardButton('Квадроцикл', callback_data='kvadro')
bike_button = types.InlineKeyboardButton('Мотоцикл', callback_data='moto')
snowmobile_button = types.InlineKeyboardButton('Снегоход', callback_data='snego')
preowned_button = types.InlineKeyboardButton('С пробегом', callback_data='preowned')

choose_technic_keyboard = types.InlineKeyboardMarkup()
choose_technic_keyboard.add(atv_button).add(bike_button).add(snowmobile_button).add(preowned_button)
