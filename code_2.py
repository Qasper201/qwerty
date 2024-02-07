import asyncio
import logging
import random

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


kb = [
    [KeyboardButton(text="Мультіплекс",), KeyboardButton(text="Планета кіно"),KeyboardButton(text="Магнат")]]
keyboard = ReplyKeyboardMarkup(keyboard=kb)

kb1 = [KeyboardButton(text="Купити білет",), KeyboardButton(text="Афіша кіно на сьогодні"),KeyboardButton(text="Додати грошей на карту")],
[KeyboardButton(text="Наші адреси"), KeyboardButton(text="Розробники бота"),KeyboardButton(text="Баланс карти")]

keyboard1 = ReplyKeyboardMarkup(keyboard=kb1)

logging.basicConfig(level=logging.INFO)
bot = Bot(token = "6555614063:AAGatIRDW558XJpHl47jJXjnKEyv0lJ6vrQ")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_answer(message: types.Message):
    await message.answer("Привіт я твій бот для кіно. Обери кінотеатр яку ти хочеш",reply_markup=keyboard)

@dp.message(F.text == "Мультіплекс")
async def cmd_answer(message: types.Message):
   await message.answer("Привіт я твій бот для кіно. Обери кінотеатр яку ти хочеш",reply_markup=keyboard1)