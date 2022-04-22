from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URL_APP, URL_MENU, URL_RESTAURANT, URL_FACEBOOK, URL_INSTAGRAM
from keyboards.inline.callback_dates import buy_callback

choice = InlineKeyboardMarkup(row_width=2)

buy_pear = InlineKeyboardButton(text="RESTAURANT", callback_data=buy_callback.new(item_name="pear", quantity=1))
choice.insert(buy_pear)

buy_apples = InlineKeyboardButton(text="APP", callback_data="buy:apple:5")
choice.insert(buy_apples)

buy_cross = InlineKeyboardButton(text="INSTAGRAM", callback_data="buy:market:5")
choice.insert(buy_cross)

buy_ticket = InlineKeyboardButton(text="FACEBOOK", callback_data="buy:ticket:5")
choice.insert(buy_ticket)

buy_about = InlineKeyboardButton(text="MENU", callback_data="buy:app:5")
choice.insert(buy_about)

cancel_button = InlineKeyboardButton(text="Cancel", callback_data="cancel")
choice.insert(cancel_button)

pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Visit", url=URL_RESTAURANT)
    ]
])
apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="visit", url=URL_APP)
    ]
])
buy_about = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="visit", url=URL_INSTAGRAM)
    ]
])
buy_ticket = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="visit", url=URL_FACEBOOK)
    ]
])
buy_cross = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="visit", url=URL_MENU)
    ]
])
