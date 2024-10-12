from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb_1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация'),
            KeyboardButton(text='Купить')
        ]
    ], resize_keyboard=True
)


kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')]
    ], resize_keyboard=True
)

produkt_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Produkt1', callback_data='product_buying')],
        [InlineKeyboardButton(text='Produkt2', callback_data='product_buying')],
        [InlineKeyboardButton(text='Produkt3', callback_data='product_buying')],
        [InlineKeyboardButton(text='Produkt4', callback_data='product_buying')]
    ], resize_keyboard=True

)