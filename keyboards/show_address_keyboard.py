from aiogram import types


def address_keyboard_maker(url: str) -> types.InlineKeyboardMarkup:
    address_button = types.InlineKeyboardButton('Показать на карте ➡️', url=url)
    phone_button = types.InlineKeyboardButton('Позвонить', url='https://atvarmor.ru/call-atvarmor')
    address_keyboard = types.InlineKeyboardMarkup()
    address_keyboard.add(address_button).add(phone_button)
    return address_keyboard
