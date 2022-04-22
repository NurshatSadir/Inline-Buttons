import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_dates import buy_callback
from keyboards.inline.choice_buttons import choice, pear_keyboard, apples_keyboard, buy_cross, buy_ticket, buy_about
from loader import dp, bot

@dp.message_handler(Command("start"))
async def show_items(message: Message):
    await message.answer(text="Choose one of them:",
                         reply_markup=choice)

@dp.callback_query_handler(text_contains="restaurant")
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data

    logging.info(f"{callback_data=}")

    await call.message.answer("You choise visit site. Good luck.",
                              reply_markup=pear_keyboard)

@dp.callback_query_handler(buy_callback.filter(item_name="app"))
async def buying_apples(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    logging.info(f"{callback_data=}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"You chose App. Good luck.",
                              reply_markup=apples_keyboard)

@dp.callback_query_handler(buy_callback.filter(item_name="instagram"))
async def buying_app(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    logging.info(f"{callback_data=}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"You chose Instagram. Good luck.",
                              reply_markup=buy_about)

@dp.callback_query_handler(buy_callback.filter(item_name="facebook"))
async def buying_ticket(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    logging.info(f"{callback_data=}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"You chose Facebook. Good luck.",
                              reply_markup=buy_ticket)

@dp.callback_query_handler(buy_callback.filter(item_name="menu"))
async def buying_market(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    logging.info(f"{callback_data=}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"You chose Menu. Good luck.",
                              reply_markup=buy_cross)

@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    await call.answer("You've canceled!", show_alert=True)

    await call.message.edit_reply_markup(reply_markup=None)