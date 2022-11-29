from aiogram import types

from loader import dp, bot
from utils import NewsParser, make_address


@dp.callback_query_handler(lambda c: c.data in ['moskva', 'podolsk'])
async def show_moscow_on_map(callback_query: types.CallbackQuery):
    np = NewsParser()
    news = np.get_address()
    post = make_address(news[callback_query.data])
    await bot.send_message(
        callback_query.from_user.id,
        post['text'],
        reply_markup=post['keyboard']
    )
