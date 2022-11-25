from aiogram import types


whats_new_button = types.KeyboardButton('💡Что нового')
sales_button = types.KeyboardButton('⭐Акции')
spare_parts_button = types.KeyboardButton('⚙️Найти запчасть')
buy_technic_button = types.KeyboardButton('🏍️Купить технику')
events_button = types.KeyboardButton('🗓️Мероприятия')
address_button = types.KeyboardButton('📍Контакты салонов')
help_button = types.KeyboardButton('🙋🏻‍♂️Задать вопрос сотруднику')


main_menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu_keyboard.add(whats_new_button, sales_button)
main_menu_keyboard.add(spare_parts_button, buy_technic_button)
main_menu_keyboard.add(address_button, events_button)
main_menu_keyboard.add(help_button)
