import sqlite3

from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database
from keyboards.inline_buttons import questionnaire_keyboard
# from scraping.news_scraper import Supernatural
# from scraping.async_news import AsyncScraper
# import re


async def start_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Python or Mojo ?",
        reply_markup=await questionnaire_keyboard()
    )


async def python_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="U R Python Developer 🐍"
    )


async def mojo_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="U R Mojo Developer 🔥"
    )

# async def async_service_call(call: types.CallbackQuery):
#     # data = await AsyncScraper().async_scrapers()
#     data = await AsyncScraper().async_scrapers()
#     links = AsyncScraper.PLUS_URL
#     for link in data:
#         await bot.send_message(chat_id=call.from_user.id,
#                                text=f"Services O!:"
#                                f"\n{links}{link}", reply_markup=await())

# async def season_call(call: types.CallbackQuery):
#     scraper = Supernatural()
#     links = scraper.parse_data()
#     for link in links:
#         await bot.send_message(
#             chat_id=call.from_user.id,
#             text=scraper.PLUS_URL + link,
#         )




def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(python_call,
                                       lambda call: call.data == "python")
    dp.register_callback_query_handler(mojo_call,
                                       lambda call: call.data == "mojo")
    # dp.register_callback_query_handler(season_call,
    #                                    lambda call: call.data == "Supernatural_season")
    # dp.register_callback_query_handler(async_service_call,
    #                                    lambda call: call.data == "save_service")