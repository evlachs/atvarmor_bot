from aiogram import types


def see_more_keyboard_maker(url):
    check_news_button = types.InlineKeyboardButton('Посмотреть на сайте ➡️', url=url)
    switch_news_keyboard = types.InlineKeyboardMarkup()
    switch_news_keyboard.add(check_news_button)
    return switch_news_keyboard
