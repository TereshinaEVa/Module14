from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio
from config import *
from keyboards_2 import *
from crud_functions import *

bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    gender = State()
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer(text='Выберите опцию:', reply_markup=kb)

@dp.message_handler(text='Регистрация')
async def regisrtration(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()
@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = get_all_products()
    for i in range(4):
        with open(f'imeges/{i+1}.jpg', 'rb') as img:
            await message.answer_photo(img, f'Название: {products[i][1]} | Описание: {products[i][2] } | Цена: {products[i][3]}')
    await message.answer(text='Выберите продукт для покупки:', reply_markup=produkt_kb)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(
        'Обращаю Ваше внимание, что данная формула актуальна только для лиц в возрасте от 13 до 80 лет.\n \
        Для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.\n \
        Для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()
@dp.callback_query_handler(text='calories')
async def set_gender(call):
    await call.message.answer('Укажите свой пол в формате f/m')
    await call.answer()
    await UserState.gender.set()

@dp.message_handler(state=UserState.gender)
async def set_age(message, state):
    await state.update_data(gender=message.text)
    await message.answer('Введите свой возраст:')
    await UserState.age.set()
@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    if data['gender'] == 'f':
        kall = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] - 161
    else:
        kall = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] + 5
    await message.answer(f'Норма каллорий: {kall}')
    await state.finish()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if is_included(message.text):
        await message.answer('Пользователь существует, введите другое имя:')
        await RegistrationState.username.set()
    else:
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=int(message.text))
    data = await state.get_data()
    username, email, age = data['username'], data['email'], data['age']
    add_user(username, email, age)
    await message.answer('Вы зарегистрированы!')
    await state.finish()
@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb_1)


@dp.message_handler()
async def all_massages(massage):
    await massage.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
