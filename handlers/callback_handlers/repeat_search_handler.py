from aiogram import types
from aiogram.dispatcher import FSMContext

from states import Form
from loader import dp, bot
from messages import MESSAGES


@dp.callback_query_handler(lambda c: c.data == 'repeat_search')
async def set_part_mark(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(Form.part_mark)
    await bot.send_message(callback_query.from_user.id, MESSAGES['set_part_mark'])
