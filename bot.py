from aiogram import Bot, Dispatcher, executor, types
import os

API_TOKEN = os.getenv("API_TOKEN")  # токен хранится в переменных окружения

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer("Добро пожаловать в наш ресторан! Напишите /menu чтобы увидеть блюда.")

@dp.message_handler(commands=['menu'])
async def show_menu(message: types.Message):
    await message.answer("Меню:\n🍲 Борщ\n🥟 Пельмени\nВведите /order <название блюда>")

@dp.message_handler(commands=['order'])
async def take_order(message: types.Message):
    order = message.text.replace("/order ", "")
    await message.answer(f"Ваш заказ: {order}. Отправлен на кухню!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
