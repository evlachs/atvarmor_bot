from aiogram import types


urls = {
    'atv': 'https://atvarmor.ru/cat/atv',
    'bike': 'https://atvarmor.ru/cat/moto',
    'snowmobile': 'https://atvarmor.ru/cat/snowmobiles',
    'preowned': 'https://atvarmor.ru/cat/preowned'
}


atv_button = types.InlineKeyboardButton('Посмотреть на сайте ➡️', url=urls['atv'])
bike_button = types.InlineKeyboardButton('Посмотреть на сайте ➡️', url=urls['bike'])
snowmobile_button = types.InlineKeyboardButton('Посмотреть на сайте ➡️', url=urls['snowmobile'])
preowned_button = types.InlineKeyboardButton('Посмотреть на сайте ➡️', url=urls['preowned'])


see_atv_keyboard = types.InlineKeyboardMarkup()
see_atv_keyboard.add(atv_button)

see_bike_keyboard = types.InlineKeyboardMarkup()
see_bike_keyboard.add(bike_button)

see_snowmobile_keyboard = types.InlineKeyboardMarkup()
see_snowmobile_keyboard.add(snowmobile_button)

see_preowned_keyboard = types.InlineKeyboardMarkup()
see_preowned_keyboard.add(preowned_button)

