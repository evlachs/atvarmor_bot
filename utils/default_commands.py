from aiogram.types import BotCommand


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            BotCommand('hide_menu', 'скрыть меню'),
            BotCommand('show_menu', 'показать меню'),
        ]
    )
