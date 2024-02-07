import asyncio
import logging
import random

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


kb = [
    [KeyboardButton(text="Купити білет",), KeyboardButton(text="Афіша кіно на сьогодні"),KeyboardButton(text="Додати грошей на карту")],
    [KeyboardButton(text="Наші адреси"), KeyboardButton(text="Розробники бота"),KeyboardButton(text="Баланс карти")]
]
keyboard = ReplyKeyboardMarkup(keyboard=kb)

logging.basicConfig(level=logging.INFO)
bot = Bot(token = "6555614063:AAGatIRDW558XJpHl47jJXjnKEyv0lJ6vrQ")
dp = Dispatcher()


@dp.message(F.text == "Додати грошей на карту")
async def cmd_answer(message: types.Message):
    buttons2 = [
        [
            InlineKeyboardButton(text="Поповнити на 500 грн", callback_data="nuй_decr")
        ],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons2)

    await message.answer(
        "На скількі хочете поповнити карту",
        reply_markup=keyboard)
    
@dp.callback_query(F.data == "nuй_decr")
async def send_random_value(callback: types.CallbackQuery):
    with open ("Баланс.txt","r+") as file:
     balans = int(file.read()) 
     balans = balans + 500
     file.write(str(balans))
    
    await callback.message.answer(f"Ваш баланс складає" + balans)




@dp.message(Command("start"))
async def cmd_answer(message: types.Message):
    await message.answer("Привіт я твій бот для кіно. Обери функцію яку ти хочеш",reply_markup=keyboard)



@dp.message(F.text == "Купити білет")
async def cmd_answer(message: types.Message):
    buttons1 = [
        [
            InlineKeyboardButton(text="На фільм Інтерстеллар (230 грн)", callback_data="num_decr")
        ],
        [    
            InlineKeyboardButton(text="На фільм Паразити (200 грн)", callback_data="num_incr")
        ],
        [    
            InlineKeyboardButton(text="На фільм Недоторканні (210 грн)", callback_data="num_decе")
        ] ,  
        [ 
            InlineKeyboardButton(text="На фільм Найкращий стрілець: Маверік (220 грн)", callback_data="num_decь")
        ],
        [   
            InlineKeyboardButton(text="На фільм Шалений Макс: Дорога гніву (170 грн)", callback_data="num_decа")
        ], 
        [    
            InlineKeyboardButton(text="На фільм У центрі уваги (190 грн)", callback_data="num_decі")
        ],
        [   
            InlineKeyboardButton(text="На фільм Аутсайдери (150 грн)", callback_data="num_decш")
        ],
        ]
       
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons1)


    await message.answer(
        "Вибіріть фільм",
        reply_markup=keyboard)

@dp.callback_query(F.data == "num_decr")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer("Ви купили білет на фільм Інтерстеллар за 230 грн, на " + str(random.randint(1, 10)) + " ряду, на місці " + str(random.randint(1, 10)))

@dp.callback_query(F.data == "num_incr")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer("Ви купили білет на фільм Паразити за 200 грн на " + str(random.randint(1, 10)) + " ряду, на місці " + str(random.randint(1, 10)))

@dp.callback_query(F.data == "num_decе")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer("Ви купили білет на фільм Недоторканні за 210 грн на " + str(random.randint(1, 10)) + " ряду, на місці " + str(random.randint(1, 10)))

@dp.callback_query(F.data == "num_decь")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer("Ви купили білет на фільм Найкращий стрілець: Маверік за 200 грн на " + str(random.randint(1, 10)) + " ряду, на місці " + str(random.randint(1, 10)))

@dp.callback_query(F.data == "num_decа")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer("Ви купили білет на фільм Шалений Макс: Дорога гніву за 170 грн на " + str(random.randint(1, 10)) + " ряду, на місці " + str(random.randint(1, 10)))

@dp.callback_query(F.data == "num_decі")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer("Ви купили білет на фільм У центрі уваги 190 грн на " + str(random.randint(1, 10)) + " ряду, на місці " + str(random.randint(1, 10)))

@dp.callback_query(F.data == "num_decш")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer("Ви купили білет на фільм На фільм Аутсайдери 150 грн на " + str(random.randint(1, 10)) + " ряду, на місці " + str(random.randint(1, 10)))

@dp.message(F.text == "Наші адреси")
async def cmd_answer(message: types.Message):
    await message.answer("Наші кінотеатри за адресою: Пушкіна 13, Кільцева 9б, Новорічна 48")   
         
@dp.message(F.text == "Афіша кіно на сьогодні")
async def cmd_answer(message: types.Message):
    await message.answer("Інтерстеллар 14:20  Паразити 15:20  Недоторканні 18:30  Шалений Макс 17:40  Дорога гніву 20:00  У центрі уваги 16:40  Аутсайдери 21:30")

@dp.message(F.text == "Розробники бота")
async def cmd_answer(message: types.Message):
    await message.answer("Рома, Влад, Саша")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())