from aiogram import types

from loader import dp, bot
from utils import NewsParser
from keyboards import see_atv_keyboard, see_bike_keyboard, see_snowmobile_keyboard, see_preowned_keyboard


@dp.callback_query_handler(lambda c: c.data == 'kvadro')
async def buy_atv(callback_query: types.CallbackQuery):
    np = NewsParser()
    tech = np.get_tech()
    post = tech[callback_query.data]
    await bot.send_photo(
        callback_query.from_user.id,
        post['img'],
        post['content'],
        reply_markup=see_atv_keyboard
    )


@dp.callback_query_handler(lambda c: c.data == 'moto')
async def buy_atv(callback_query: types.CallbackQuery):
    np = NewsParser()
    tech = np.get_tech()
    post = tech[callback_query.data]
    await bot.send_photo(
        callback_query.from_user.id,
        post['img'],
        post['content'],
        reply_markup=see_bike_keyboard
    )


@dp.callback_query_handler(lambda c: c.data == 'snego')
async def buy_atv(callback_query: types.CallbackQuery):
    np = NewsParser()
    tech = np.get_tech()
    post = tech[callback_query.data]
    await bot.send_photo(
        callback_query.from_user.id,
        post['img'],
        post['content'],
        reply_markup=see_snowmobile_keyboard
    )


@dp.callback_query_handler(lambda c: c.data == 'preowned')
async def buy_atv(callback_query: types.CallbackQuery):
    np = NewsParser()
    tech = np.get_tech()
    post = tech[callback_query.data]
    await bot.send_photo(
        callback_query.from_user.id,
        post['img'],
        post['content'],
        reply_markup=see_preowned_keyboard
    )
