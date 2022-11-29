from aiogram import types
from aiogram.dispatcher import FSMContext

from states import Form
from loader import dp, bot
from keyboards import manager_keyboard, repeat_search_keyboard
from utils import NewsParser, make_post_message


@dp.message_handler(state=Form.part_mark)
async def send_sales(message: types.Message, state: FSMContext):
    np = NewsParser()
    news = np.get_spare_part(message.text)
    keyboard = manager_keyboard.add(repeat_search_keyboard)
    if isinstance(news, str):
        await bot.send_message(message.chat.id, news, reply_markup=keyboard)
        await state.finish()
        return
    post = make_post_message(news)
    await dp.bot.send_message(
        message.chat.id,
        post['text'],
        reply_markup=post['keyboard']
    )
    await state.finish()
