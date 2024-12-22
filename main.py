import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
import random

from gtts import gTTS
import os

from config import TOKEN
import keyboard as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.callback_query(F.data == 'news')
async def news(callback: CallbackQuery):
   await callback.answer("Новости подгружаются", show_alert=True)
   await callback.message.edit_text('Вот свежие новости!', reply_markup=await kb.news_keyboard())

@dp.callback_query(F.data == 'video')
async def news(callback: CallbackQuery):
   await callback.answer("Видео подгружаются", show_alert=True)
   await callback.message.edit_text('Видео можно найти здесь!', reply_markup=await kb.video_keyboard())

@dp.callback_query(F.data == 'music')
async def news(callback: CallbackQuery):
   await callback.answer("Музыка подгружается", show_alert=True)
   await callback.message.edit_text('Музыка!', reply_markup=await kb.music_keyboard())

@dp.message(F.text == "Тестовая кнопка 1")
async def test_button(message: Message):
   await message.answer('Обработка нажатия на reply кнопку')

@dp.message(Command('help'))
async def help(message: Message):
   await message.answer('Этот бот умеет выполнять команды: \n /start \n /help \n /links \n /dynamic')
#-
@dp.message(CommandStart())
async def start(message: Message):
    user = message.from_user
    await message.answer(f"Привет, {user.first_name}!", reply_markup=kb.start_keyboard)

# Обработка кнопки "Привет"
@dp.message(lambda message: message.text == "Привет")
async def greet_user(message: Message):
    user = message.from_user
    await message.answer(f"Привет, {user.first_name}!")

# Обработка кнопки "Пока"
@dp.message(lambda message: message.text == "Пока")
async def goodbye_user(message: Message):
    user = message.from_user
    await message.answer(f"До свидания, {user.first_name}!")
#-

@dp.message(Command("links"))
async def links(message: Message):
    await message.answer("Выберите тип контента:", reply_markup=kb.inline_keyboard_test)
    
@dp.message(Command("dynamic"))
async def cmd_dynamic(message: Message):
    # Отправляем начальную клавиатуру с кнопкой "Показать больше"
    await message.answer("Нажмите кнопку ниже:", reply_markup=kb.dynamic_keyboard())

# Обработка нажатия на кнопку "Показать больше"
@dp.callback_query(lambda c: c.data == "show_more")
async def show_more(callback_query: CallbackQuery):
    # Заменяем клавиатуру на две новые кнопки
    await bot.edit_message_text(
        "Выберите одну из опций:",
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        reply_markup=kb.options_keyboard()
    )

# Обработка выбора "Опция 1" или "Опция 2"
@dp.callback_query(lambda c: c.data == "option_1")
async def option_1(callback_query: CallbackQuery):
    # Ответ на выбор "Опция 1"
    await bot.edit_message_text(
        "Вы выбрали Опцию 1.",
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id
    )

@dp.callback_query(lambda c: c.data == "option_2")
async def option_2(callback_query: CallbackQuery):
    # Ответ на выбор "Опция 2"
    await bot.edit_message_text(
        "Вы выбрали Опцию 2.",
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id
    )

async def main():
   await dp.start_polling(bot)

if __name__ == '__main__':
   asyncio.run(main())
