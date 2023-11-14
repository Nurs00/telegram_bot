from aiogram import types, Dispatcher
from config import bot, DESTINATION
from database.sql_commands import Database


async def start_button(message: types.Message):
    print(message)
    Database().sql_insert_users(telegram_id=message.from_user.id,
                                username=message.from_user.username,
                                first_name=message.from_user.first_name,
                                last_name=message.from_user.last_name,)

    # await bot.send_message(
    #     chat_id=message.from_user.id,
    #     text=f"Hi {message.from_user.first_name}"
    # )
    with open(DESTINATION + "/voicebot.jpg", 'rb') as photo:
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo
        )




def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=['start'])