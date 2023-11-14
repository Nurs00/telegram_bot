import sqlite3

from aiogram import types, Dispatcher
from config import bot, DESTINATION
from profanity_check import predict_prob


async def chat_messages(message: types.Message):
    print(message)
    if message.chat.id == -1002121075172:
        ban_word_predict_prob = predict_prob([message.text])
        if ban_word_predict_prob > 0.1:
            await message.delete()
            await bot.send_message(
                chat_id=message.chat.id,
                text=f"User: {message.from_user.id} {message.from_user.first_name}\n"
                     f"не матерись, мать смотрит!!!"
        )

    else:
        await message.reply(
            text="Такой команды не существует!!!"
        )


def register_chat_actions_handlers(dp: Dispatcher):
    dp.register_message_handler(chat_messages)
