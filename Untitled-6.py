[
                #InlineKeyboardButton(text="На фільм Інтерстеллар (230 грн)", callback_data="num_decr")
            ],
            [    
                InlineKeyboardButton(text="На фільм Паразити (200 грн)", callback_data="num_incr")
            ],
            [    
                #InlineKeyboardButton(text="На фільм Недоторканні (210 грн)", callback_data="num_decе")
            ] ,  
            [ 
                InlineKeyboardButton(text="На фільм Найкращий стрілець: Маверік (220 грн)", callback_data="num_decь")
            ],
            [   
                #InlineKeyboardButton(text="На фільм Шалений Макс: Дорога гніву (170 грн)", callback_data="num_decа")
            ], 
            [    
                #InlineKeyboardButton(text="На фільм У центрі уваги (190 грн)", callback_data="num_decі")
            ],
            [   
                #InlineKeyboardButton(text="На фільм Аутсайдери (150 грн)", callback_data="num_decш")
            ]


("""Карамельний маленький - 60грн    середній - 100грн    великий - 150грн\n
    Чіпси маленькі - 40грн    середні - 65грн    великі - 100грн\n
    Сирний маленький - 65грн    середній - 100грн    великий - 170грн\n
    Шоколадний маленький - 75грн    середній - 105грн    великий - 165грн

    """)

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
            #@dp.callback_query(F.data == "num_decr")
    #async def send_random_value(callback: types.CallbackQuery):
            



             @dp.callback_query(F.data == "1_1")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 230:
           
            number -= 230
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Інтерстеллар за 230 грн на 1 ряду, на 1 місці ")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")


    @dp.callback_query(F.data == "1_2")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 230:
           
            number -= 230
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Інтерстеллар за 230 грн на 1 ряду, на 2 місці ")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")        
    
    @dp.callback_query(F.data == "1_3")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 230:
           
            number -= 230
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Інтерстеллар за 230 грн на 1 ряду, на 3 місці ")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")
    

    @dp.callback_query(F.data == "1_4")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 230:
           
            number -= 230
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Інтерстеллар за 230 грн на 1 ряду, на 4 місці ")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")
    

    @dp.callback_query(F.data == "1_5")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 230:
           
            number -= 230
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Інтерстеллар за 230 грн на 1 ряду, на 5 місці ")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")

    
    @dp.callback_query(F.data == "1_6")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 230:
           
            number -= 230
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Інтерстеллар за 230 грн на 1 ряду, на 6 місці ")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")
    
    @dp.callback_query(F.data == "2_1")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 230:
           
            number -= 230
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Інтерстеллар за 230 грн на 2 ряду, на 1 місці ")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")


    @dp.callback_query(F.data == "2_2")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 230:
           
            number -= 230
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Інтерстеллар за 230 грн на 2 ряду, на 2 місці ")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")        
    
    @dp.callback_query(F.data == "2_3")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 230:
           
            number -= 230
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Інтерстеллар за 230 грн на 2 ряду, на 3 місці ")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")
    

    @dp.callback_query(F.data == "2_4")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 230:
           
            number -= 230
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Інтерстеллар за 230 грн на 2 ряду, на 4 місці ")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")
    

    @dp.callback_query(F.data == "2_5")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 230:
           
            number -= 230
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Інтерстеллар за 230 грн на 2 ряду, на 5 місці ")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")

    
    @dp.callback_query(F.data == "2_6")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 230:
           
            number -= 230
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Інтерстеллар за 230 грн на 2 ряду, на 6 місці ")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")

    @dp.callback_query(F.data == "3_1")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 230:
           
            number -= 230
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Інтерстеллар за 230 грн на 3 ряду, на 1 місці ")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")


    @dp.callback_query(F.data == "3_2")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 230:
           
            number -= 230
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Інтерстеллар за 230 грн на 3 ряду, на 2 місці ")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")        
    
    @dp.callback_query(F.data == "3_3")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 230:
           
            number -= 230
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Інтерстеллар за 230 грн на 3 ряду, на 3 місці ")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")
    

    @dp.callback_query(F.data == "3_4")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 230:
           
            number -= 230
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Інтерстеллар за 230 грн на 3 ряду, на 4 місці ")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")
    

    @dp.callback_query(F.data == "3_5")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 230:
           
            number -= 230
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Інтерстеллар за 230 грн на 3 ряду, на 5 місці ")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")

    
    @dp.callback_query(F.data == "3_6")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 230:
           
            number -= 230
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Інтерстеллар за 230 грн на 3 ряду, на 6 місці ")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")
