from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Тестовая кнопка 1")],
   [KeyboardButton(text="Тестовая кнопка 2"), KeyboardButton(text="Тестовая кнопка 3")]
], resize_keyboard=True)

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Видео", callback_data='video')],
   [InlineKeyboardButton(text="Новости", callback_data='news')],
   [InlineKeyboardButton(text="Музыка", callback_data='music')]
])

news_list = ["Новости Дзен"]

async def news_keyboard():
   keyboard = InlineKeyboardBuilder()
   for key in news_list:
       keyboard.add(InlineKeyboardButton(text=key, url='https://dzen.ru/news'))
   return keyboard.adjust(2).as_markup()

video_list = ["Видео YouTube"]

async def video_keyboard():
   keyboard = InlineKeyboardBuilder()
   for key in video_list:
       keyboard.add(InlineKeyboardButton(text=key, url='https://www.youtube.com/'))
   return keyboard.adjust(2).as_markup()

music_list = ["Музыка яндекс"]

async def music_keyboard():
   keyboard = InlineKeyboardBuilder()
   for key in music_list:
       keyboard.add(InlineKeyboardButton(text=key, url='https://music.yandex.ru/home'))
   return keyboard.adjust(2).as_markup()

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет")],
        [KeyboardButton(text="Пока")]
    ],
    resize_keyboard=True  # Уменьшение клавиатуры для мобильных устройств
)

def links_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text="Новости", url="https://news.ycombinator.com/"),
        InlineKeyboardButton(text="Видео", url="https://www.youtube.com/"),
        InlineKeyboardButton(text="Музыка", url="https://www.spotify.com/")
    )
    return keyboard

def dynamic_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Показать больше", callback_data="show_more")]
    ])
    return keyboard

# Клавиатура с кнопками "Опция 1" и "Опция 2"
def options_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Опция 1", callback_data="option_1")],
        [InlineKeyboardButton(text="Опция 2", callback_data="option_2")]
    ])
    return keyboard
