import asyncio
import logging
import random

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

logging.basicConfig(level=logging.INFO)
bot = Bot(token = "6555614063:AAGatIRDW558XJpHl47jJXjnKEyv0lJ6vrQ")
dp = Dispatcher()


cinemas = {"Мультіплекс","Планета кіно","Магнат"}



kb1 = [
    [KeyboardButton(text="Додати грошей на карту"),KeyboardButton(text="Їжа та її вартість"),KeyboardButton(text="Купити їжу"),KeyboardButton(text="Наші адреси")],
    [KeyboardButton(text="Купити білет"),KeyboardButton(text="Баланс карти"),KeyboardButton(text="Афіша кіно на сьогодні"),KeyboardButton(text="Розробники бота")]
    ]
keyboard1 = ReplyKeyboardMarkup(keyboard=kb1)


kb = [
    [KeyboardButton(text="Мультіплекс",), KeyboardButton(text="Планета кіно"),KeyboardButton(text="Магнат")]]
keyboard = ReplyKeyboardMarkup(keyboard=kb)

@dp.message(F.text.in_(cinemas))
async def cmd_answer(message: types.Message):
    with open("кінотеатр.txt","w") as file:
        file.write(message.text)
    await message.answer("Дякую що обрали кінотеатр",reply_markup = keyboard1 )
    
@dp.message(Command("start"))
async def cmd_answer(message: types.Message):
    await message.answer("Привіт, я твій бот для кіно обери кінотеатр", reply_markup = keyboard)

with open("кінотеатр.txt","r") as file:
    cought_cinema = file.read()















if cought_cinema == "Мультіплекс":
    
    @dp.message(F.text == "Додати грошей на карту")
    async def cmd_answer(message: types.Message):
        buttons2 = [
            [
                InlineKeyboardButton(text="Поповнити на 500 грн", callback_data="nuй_decr")
            ],
            [
                InlineKeyboardButton(text="Поповнити на 250 грн", callback_data="nuц_decr")
            ],
            [
                InlineKeyboardButton(text="Поповнити на 100 грн", callback_data="nuу_decr")
            ],
        ]

        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons2)

        await message.answer(
            "На скількі хочете поповнити карту",
            reply_markup=keyboard)
    
    @dp.callback_query(F.data == "nuй_decr")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        number += 500

        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        
        await callback.message.answer(f"Ваш баланс складає {number}" )

    @dp.callback_query(F.data == "nuц_decr")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        number += 250

        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        
        await callback.message.answer(f"Ваш баланс складає {number}" )

    @dp.callback_query(F.data == "nuу_decr")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        number += 100

        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        
        await callback.message.answer(f"Ваш баланс складає {number}" )

    @dp.message(F.text == "Купити білет")
    async def cmd_answer(message: types.Message):
        buttons1 = [
            [
                InlineKeyboardButton(text="На фільм Інтерстеллар (230 грн)",callback_data="num_decr" )
            ],           
            [    
                InlineKeyboardButton(text="На фільм Недоторканні (210 грн)", callback_data="num_decе")
            ] ,             
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
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 230:
           
            number -= 230
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Інтерстеллар за 230 грн, на " + str(random.randint(1, 10)) + " ряду, на місці " + str(random.randint(1, 10)))
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")
            
   
    @dp.callback_query(F.data == "num_dece")
    async def send_random_value(callback: types.CallbackQuery):  
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 210:
           
            number -= 210
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Недоторканні за 210 грн, на " + str(random.randint(1, 10)) + " ряду, на місці " + str(random.randint(1, 10)))
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")
            


    @dp.callback_query(F.data == "num_decі")   
    async def send_random_value(callback: types.CallbackQuery):
     file = open("Баланс.txt", 'r')
     number = int(file.read())
     file.close()
 
     if number >= 190:
    
         number -= 190
         file = open("Баланс.txt", 'w')
         file.write(str(number))
         file.close()
         await callback.message.answer("Ви купили білет на фільм У центрі уваги: Маверік за 190 грн, на " + str(random.randint(1, 10)) + " ряду, на місці " + str(random.randint(1, 10)))
     else:
         await callback.message.answer("На вашому балансі не вистачає грошей")
 
    @dp.callback_query(F.data == "num_decш")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 150:
        
            number -= 150
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм На фільм Аутсайдери за 150 грн, на " + str(random.randint(1, 10)) + " ряду, на місці " + str(random.randint(1, 10)))
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")
    




    @dp.message(F.text == "Їжа та її вартість")
    async def cmd_answer(message: types.Message):
        await message.answer("""
    Карамельний маленький - 60грн    середній - 100грн    великий - 150грн\n
    Чіпси маленькі - 40грн    середні - 65грн    великі - 100грн\n
    Сирний маленький - 65грн    середній - 100грн    великий - 170грн\n
    """)


    @dp.message(F.text == "Купити їжу")
    async def cmd_answer(message: types.Message):
        buttons2 = [
            [
                InlineKeyboardButton(text="карамельний маленький", callback_data="a")
            ],
            [
                InlineKeyboardButton(text="карамельний середній", callback_data="b")
            ],
            [
                InlineKeyboardButton(text="карамельний великий", callback_data="c")
            ],
            [
                InlineKeyboardButton(text="Чіпси маленькі", callback_data="d")
            ],
            [
                InlineKeyboardButton(text="Чіпси середні", callback_data="e")
            ],
            [
                InlineKeyboardButton(text="Чіпси великі", callback_data="f")
            ],
            [
                InlineKeyboardButton(text="сирний маленький", callback_data="g")
            ],
            [
                InlineKeyboardButton(text="сирний середній", callback_data="h")
            ],
            [
                InlineKeyboardButton(text="сирний великий", callback_data="i")
            ],
            
            
            ]

        kb = InlineKeyboardMarkup(inline_keyboard=buttons2)


        await message.answer(
            "Вибіріть попкорн",
            reply_markup=kb)

    @dp.callback_query(F.data == "a")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 60:
        
            number -= 60
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили маленький попкорн зі смаком карамелі")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")
 
    @dp.callback_query(F.data == "b")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 100:
        
            number -= 100
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили середній попкорн зі смаком карамелі")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")

    @dp.callback_query(F.data == "c")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 150:
        
            number -= 150
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили великій попкорн зі смаком карамелі")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")

    @dp.callback_query(F.data == "d")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 40:
        
            number -= 40
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили маленький попкорн зі смаком бекону")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")


    @dp.callback_query(F.data == "e")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 65:
        
            number -= 65
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили середній попкорн зі смаком бекону")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")


    @dp.callback_query(F.data == "f")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 100:
        
            number -= 100
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили великій зі смаком бекону")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")


    @dp.callback_query(F.data == "g")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >=65:
        
            number -= 65
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили маленький зі смаком сиру")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")


    @dp.callback_query(F.data == "h")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >=100:
        
            number -= 100
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили середній зі смаком сиру")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")

    @dp.callback_query(F.data == "i")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >=170:
        
            number -= 170
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили великий зі смаком сиру")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")

    @dp.message(F.text == "Афіша кіно на сьогодні")
    async def cmd_answer(message: types.Message):
        await message.answer("Інтерстеллар 14:20   Недоторканні 18:30   У центрі уваги 16:40  Аутсайдери 21:30")





















if cought_cinema == "Планета кіно":
    
    @dp.message(F.text == "Додати грошей на карту")
    async def cmd_answer(message: types.Message):
        buttons2 = [
            [
                InlineKeyboardButton(text="Поповнити на 500 грн", callback_data="nuй_decr")
            ],
            [
                InlineKeyboardButton(text="Поповнити на 350 грн", callback_data="nuц_decr")
            ],
            [
                InlineKeyboardButton(text="Поповнити на 100 грн", callback_data="nuу_decr")
            ],
        ]

        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons2)

        await message.answer(
            "На скількі хочете поповнити карту",
            reply_markup=keyboard)
    
    @dp.callback_query(F.data == "nuй_decr")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        number += 500

        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        
        await callback.message.answer(f"Ваш баланс складає {number}" )

    @dp.callback_query(F.data == "nuц_decr")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        number += 350

        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        
        await callback.message.answer(f"Ваш баланс складає {number}" )

    @dp.callback_query(F.data == "nuу_decr")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        number += 100

        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        
        await callback.message.answer(f"Ваш баланс складає {number}" )

    @dp.message(F.text == "Купити білет")
    async def cmd_answer(message: types.Message):    
        buttons1 = [
            [
                InlineKeyboardButton(text="На фільм Інтерстеллар (230 грн)", callback_data="num_decr")
            ],           
            [    
                InlineKeyboardButton(text="На фільм Недоторканні (210 грн)", callback_data="num_decе")
            ] ,             
            [    
                InlineKeyboardButton(text="На фільм Найкращий стрілець: Маверік (220 грн)", callback_data="num_decі")
            ],
            [   
                InlineKeyboardButton(text="На фільм Паразити (200 грн)", callback_data="num_decш")
            ],
            ]
        
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons1)


        await message.answer(
            "Вибіріть фільм",
            reply_markup=keyboard)

    @dp.callback_query(F.data == "num_decr")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 230:
           
            number -= 230
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Інтерстеллар за 230 грн, на " + str(random.randint(1, 10)) + " ряду, на місці " + str(random.randint(1, 10)))
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")
    

    @dp.callback_query(F.data == "num_decе")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 210:
        
            number -= 210
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Недоторкані за 210 грн, на " + str(random.randint(1, 10)) + " ряду, на місці " + str(random.randint(1, 10)))
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")
    

    
    @dp.callback_query(F.data == "num_num_decі")   
    async def send_random_value(callback: types.CallbackQuery):
     file = open("Баланс.txt", 'r')
     number = int(file.read())
     file.close()
 
     if number >= 220:
    
         number -= 220
         file = open("Баланс.txt", 'w')
         file.write(str(number))
         file.close()
         await callback.message.answer("Ви купили білет на фільм Найкращий стрілець: Маверік за 220 грн, на " + str(random.randint(1, 10)) + " ряду, на місці " + str(random.randint(1, 10)))
     else:
         await callback.message.answer("На вашому балансі не вистачає грошей")
 
    @dp.callback_query(F.data == "num_decш")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 200:
        
            number -= 200
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм на фільм Gfhfpbn за 150 грн, на " + str(random.randint(1, 10)) + " ряду, на місці " + str(random.randint(1, 10)))
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")
    




    @dp.message(F.text == "Їжа та її вартість")
    async def cmd_answer(message: types.Message):
        await message.answer("""
    Карамельний маленький - 60грн    середній - 100грн    великий - 150грн\n
    Чіпси маленькі - 40грн    середні - 65грн    великі - 100грн\n
    Шоколадний маленький - 75грн    середній - 105грн    великий - 165грн
    """)


    @dp.message(F.text == "Купити їжу")
    async def cmd_answer(message: types.Message):
        buttons2 = [
            [
                InlineKeyboardButton(text="карамельний маленький", callback_data="a")
            ],
            [
                InlineKeyboardButton(text="карамельний середній", callback_data="b")
            ],
            [
                InlineKeyboardButton(text="карамельний великий", callback_data="c")
            ],
            [
                InlineKeyboardButton(text="Чіпси маленькі", callback_data="d")
            ],
            [
                InlineKeyboardButton(text="Чіпси середні", callback_data="e")
            ],
            [
                InlineKeyboardButton(text="Чіпси великі", callback_data="f")
            ],
            [
                InlineKeyboardButton(text="Шоколадний маленький", callback_data="g")
            ],
            [
                InlineKeyboardButton(text="Шоколадний середній", callback_data="h")
            ],
            [
                InlineKeyboardButton(text="Шоколадний великий", callback_data="i")
            ],
            
            
            ]

        kb = InlineKeyboardMarkup(inline_keyboard=buttons2)


        await message.answer(
            "Вибіріть попкорн",
            reply_markup=kb)

    @dp.callback_query(F.data == "a")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 60:
        
            number -= 60
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили маленький попкорн зі смаком карамелі")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")
 
    @dp.callback_query(F.data == "b")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 100:
        
            number -= 100
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили середній попкорн зі смаком карамелі")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")

    @dp.callback_query(F.data == "c")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 150:
        
            number -= 150
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили великій попкорн зі смаком карамелі")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")

    @dp.callback_query(F.data == "d")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 40:
        
            number -= 40
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили маленький попкорн зі смаком бекону")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")


    @dp.callback_query(F.data == "e")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 65:
        
            number -= 65
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили середній попкорн зі смаком бекону")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")


    @dp.callback_query(F.data == "f")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 100:
        
            number -= 100
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили великій зі смаком бекону")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")


    @dp.callback_query(F.data == "g")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >=75:
        
            number -= 75
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили маленький зі смаком сиру")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")


    @dp.callback_query(F.data == "h")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >=105:
        
            number -= 105
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили середній зі смаком сиру")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")

    @dp.callback_query(F.data == "i")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >=165:
        
            number -= 165
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили великий зі смаком сиру")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")

    @dp.message(F.text == "Афіша кіно на сьогодні")
    async def cmd_answer(message: types.Message):
        await message.answer("Інтерстеллар 14:20   Недоторканні 18:30    Найкращий стрілець: Маверік 17:25  Аутсайдери 21:30")        



















if cought_cinema == "Магнат":
    
    @dp.message(F.text == "Додати грошей на карту")
    async def cmd_answer(message: types.Message):
        buttons2 = [
            [
                InlineKeyboardButton(text="Поповнити на 500 грн", callback_data="nuй_decr")
            ],
            [
                InlineKeyboardButton(text="Поповнити на 350 грн", callback_data="nuц_decr")
            ],
            [
                InlineKeyboardButton(text="Поповнити на 100 грн", callback_data="nuу_decr")
            ],
        ]

        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons2)

        await message.answer(
            "На скількі хочете поповнити карту",
            reply_markup=keyboard)
    
    @dp.callback_query(F.data == "nuй_decr")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        number += 500

        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        
        await callback.message.answer(f"Ваш баланс складає {number}" )

    @dp.callback_query(F.data == "nuц_decr")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        number += 350

        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        
        await callback.message.answer(f"Ваш баланс складає {number}" )

    @dp.callback_query(F.data == "nuу_decr")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        number += 100

        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        
        await callback.message.answer(f"Ваш баланс складає {number}" )

    @dp.message(F.text == "Купити білет")
    async def cmd_answer(message: types.Message):    
        buttons1 = [
            [
                InlineKeyboardButton(text="На фільм У центрі уваги (190 грн)", callback_data="num_decr")
            ],           
            [    
                InlineKeyboardButton(text="На фільм Аутсайдери (150 грн)", callback_data="num_decе")
            ] ,             
            [    
                InlineKeyboardButton(text="На фільм Найкращий стрілець: Маверік (220 грн)", callback_data="num_decі")
            ],
            [   
                InlineKeyboardButton(text="На фільм Паразити (200 грн)", callback_data="num_decш")
            ],
            ]
        
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons1)


        await message.answer(
            "Вибіріть фільм",
            reply_markup=keyboard)

    @dp.callback_query(F.data == "num_decr")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 190:
           
            number -= 190
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм У центрі уваги за 230 грн, на " + str(random.randint(1, 10)) + " ряду, на місці " + str(random.randint(1, 10)))
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")
    

    @dp.callback_query(F.data == "num_decе")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 150:
        
            number -= 150
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Аутсайдери за 150 грн, на " + str(random.randint(1, 10)) + " ряду, на місці " + str(random.randint(1, 10)))
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")
    

    
    @dp.callback_query(F.data == "num_num_decі")   
    async def send_random_value(callback: types.CallbackQuery):
     file = open("Баланс.txt", 'r')
     number = int(file.read())
     file.close()
 
     if number >= 220:
    
         number -= 220
         file = open("Баланс.txt", 'w')
         file.write(str(number))
         file.close()
         await callback.message.answer("Ви купили білет на фільм Найкращий стрілець: Маверік за 220 грн, на " + str(random.randint(1, 10)) + " ряду, на місці " + str(random.randint(1, 10)))
     else:
         await callback.message.answer("На вашому балансі не вистачає грошей")
 
    @dp.callback_query(F.data == "num_decш")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 200:
        
            number -= 200
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм На фільм Аутсайдери за 150 грн, на " + str(random.randint(1, 10)) + " ряду, на місці " + str(random.randint(1, 10)))
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")
    




    @dp.message(F.text == "Їжа та її вартість")
    async def cmd_answer(message: types.Message):
        await message.answer("""
    Карамельний маленький - 60грн    середній - 100грн    великий - 150грн\n
    Чіпси маленькі - 40грн    середні - 65грн    великі - 100грн\n
    Шоколадний маленький - 75грн    середній - 105грн    великий - 165грн
    """)


    @dp.message(F.text == "Купити їжу")
    async def cmd_answer(message: types.Message):
        buttons2 = [
            [
                InlineKeyboardButton(text="карамельний маленький", callback_data="a")
            ],
            [
                InlineKeyboardButton(text="карамельний середній", callback_data="b")
            ],
            [
                InlineKeyboardButton(text="карамельний великий", callback_data="c")
            ],
            [
                InlineKeyboardButton(text="Чіпси маленькі", callback_data="d")
            ],
            [
                InlineKeyboardButton(text="Чіпси середні", callback_data="e")
            ],
            [
                InlineKeyboardButton(text="Чіпси великі", callback_data="f")
            ],
            [
                InlineKeyboardButton(text="Шоколадний маленький", callback_data="g")
            ],
            [
                InlineKeyboardButton(text="Шоколадний середній", callback_data="h")
            ],
            [
                InlineKeyboardButton(text="Шоколадний великий", callback_data="i")
            ],
            
            
            ]

        kb = InlineKeyboardMarkup(inline_keyboard=buttons2)


        await message.answer(
            "Вибіріть попкорн",
            reply_markup=kb)

    @dp.callback_query(F.data == "a")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 60:
        
            number -= 60
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили маленький попкорн зі смаком карамелі")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")
 
    @dp.callback_query(F.data == "b")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 100:
        
            number -= 100
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили середній попкорн зі смаком карамелі")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")

    @dp.callback_query(F.data == "c")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 150:
        
            number -= 150
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили великій попкорн зі смаком карамелі")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")

    @dp.callback_query(F.data == "d")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 40:
        
            number -= 40
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили маленький попкорн зі смаком бекону")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")


    @dp.callback_query(F.data == "e")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 65:
        
            number -= 65
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили середній попкорн зі смаком бекону")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")


    @dp.callback_query(F.data == "f")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 100:
        
            number -= 100
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили великій зі смаком бекону")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")


    @dp.callback_query(F.data == "g")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >=75:
        
            number -= 75
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили маленький зі смаком сиру")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")


    @dp.callback_query(F.data == "h")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >=105:
        
            number -= 105
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили середній зі смаком сиру")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")

    @dp.callback_query(F.data == "i")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >=165:
        
            number -= 165
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили великий зі смаком сиру")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")

    @dp.message(F.text == "Афіша кіно на сьогодні")
    async def cmd_answer(message: types.Message):
        await message.answer("Інтерстеллар 14:20   Недоторканні 18:30    Найкращий стрілець: Маверік 17:25  Аутсайдери 21:30")

@dp.message(F.text == "Баланс карти")
async def cmd_answer(message: types.Message):
    file1 = open("Баланс.txt", 'r')
    balans = file1.read()
    await message.answer(f"Ваш баланс {balans}") 


@dp.message(F.text == "Наші адреси")
async def cmd_answer(message: types.Message):
    await message.answer("Наші кінотеатри за адресою: Пушкіна 13, Кільцева 9б, Новорічна 48")   
         
    

@dp.message(F.text == "Розробники бота")
async def cmd_answer(message: types.Message):
    await message.answer("Рома, Саша")




async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())