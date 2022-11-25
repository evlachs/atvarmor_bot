import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext

from states import Form
from loader import dp, bot
from messages import MESSAGES
from utils import NewsParser, make_post_message
from keyboards import choose_technic_keyboard, choose_city_keyboard, manager_keyboard


@dp.message_handler(lambda msg: msg.text == '💡Что нового')
async def send_news(message: types.Message):
    np = NewsParser()
    news = np.get_news()
    for n in news:
        post = make_post_message(n)
        await bot.send_photo(
            message.chat.id,
            post['img'],
            post['text'],
            reply_markup=post['keyboard']
        )
        await asyncio.sleep(0.1)


@dp.message_handler(lambda msg: msg.text == '⭐Акции')
async def send_sales(message: types.Message):
    np = NewsParser()
    news = np.get_sales()
    for n in news:
        post = make_post_message(n)
        await bot.send_photo(
            message.chat.id,
            post['img'],
            post['text'],
            reply_markup=post['keyboard']
        )
        await asyncio.sleep(0.1)


@dp.message_handler(lambda msg: msg.text == '🗓️Мероприятия')
async def send_sales(message: types.Message):
    np = NewsParser()
    events = np.get_events()
    for e in events:
        post = make_post_message(e)
        await bot.send_photo(
            message.chat.id,
            post['img'],
            post['text'],
            reply_markup=post['keyboard']
        )
        await asyncio.sleep(0.1)


@dp.message_handler(lambda msg: msg.text == '⚙️Найти запчасть')
async def set_part_mark(message: types.Message, state: FSMContext):
    await state.set_state(Form.part_mark)
    await bot.send_message(message.chat.id, MESSAGES['set_part_mark'])


@dp.message_handler(lambda msg: msg.text == '🏍️Купить технику')
async def buy_technic(message: types.Message):
    np = NewsParser()
    tech = np.get_tech()
    post = tech['main']
    await bot.send_photo(
        message.chat.id,
        post['img'],
        post['content'],
        reply_markup=choose_technic_keyboard
    )


@dp.message_handler(lambda msg: msg.text == '📍Контакты салонов')
async def show_address(message: types.Message):
    await bot.send_message(message.chat.id, MESSAGES['choose_city'], reply_markup=choose_city_keyboard)


@dp.message_handler(lambda msg: msg.text == '🙋🏻‍♂️Задать вопрос сотруднику')
async def show_address(message: types.Message):
    await bot.send_message(message.chat.id, MESSAGES['call_manager'], reply_markup=manager_keyboard)
