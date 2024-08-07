from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


async def start_button():
    """
    Функция для создания и возврата клавиатуры с кнопками для начала различных операций.

    Действие:
        Создает и возвращает клавиатуру с кнопками для начала различных операций, таких как "Отель", "Рестораны" и "Погода".

    Возвращает:
        ReplyKeyboardMarkup: Объект клавиатуры с кнопками для начала различных операций.
    """
    key_board = ReplyKeyboardMarkup(resize_keyboard=True)

    key_board.add(KeyboardButton("/Отель")).add(
        KeyboardButton("/Рестораны")
    ).add(KeyboardButton("/Погода")).add(KeyboardButton("/История_запросов"))
    return key_board
