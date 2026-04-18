from os import getenv
import asyncio
import random  
import string  
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command, CommandObject
from dotenv import load_dotenv
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.utils.keyboard import ReplyKeyboardBuilder

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
router = Router()
dp.include_router(router)

def rps_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text='Камень🪨')
    builder.button(text='Ножницы✂️')
    builder.button(text='Бумага📄')
    builder.button(text='Стоп❌')
    builder.adjust(3) #кнопки в ряд по 3
    return builder.as_markup(resize_keyboard=True)

def generate_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@router.message(Command("password"))
async def send_password(message: types.Message, command: CommandObject):
    if command.args is None:
        length = 12
    else:
        try:
            length = int(command.args)
            if length > 100:
                return await message.answer('Слишком длинный пароль! Максимум - 100 символов.')
            if length < 4:
                return await message.answer('Пароль должен быть не короче 4 символов.')
        except ValueError:
            return await message.answer('Ошибка! После команды /password нужно написать число (длинну).')
        
    new_pass = generate_password(length)
    # Отправляем пользователю
    await message.answer(f"Твой пароль длинной в {length} символов: \n'{new_pass}'", parse_mode="HTML")

@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer('Привет! Напиши /password (число), чтобы получить случайный пароль. Введи /games если хочешь поиграть.')
    
@router.message(Command("games"))
async def games_handler(message: types.Message):
    await message.answer('Привет! Со мной можно поиграть в "угадай число" и "камень, ножницы, бумага".')
    await message.answer('Для игры "угадай число" введи /guessthenumber, а для "камень, ножницы, бумага" /suyefa.')
    
class GameStates(StatesGroup):
    waiting_for_guess = State()

@router.message(Command("guessthenumber"))
async def start_game(message: types.Message, state: FSMContext):
    secret_number = random.randint(1, 100)
    await state.update_data(secret_number=secret_number, attempts=0)
    
    await message.answer('Игра началась! Я загадал число от 1 до 100. Попробуй угадать! У тебя 10 попыток.')
    await state.set_state(GameStates.waiting_for_guess)
    
@router.message(StateFilter(GameStates.waiting_for_guess))
async def process_guess(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        return await message.answer('Пожалуйста, введите целое число!')
    
    user_guess = int(message.text)
    data = await state.get_data()
    secret_number = data['secret_number']
    attempts = data['attempts'] + 1
    max_attempts = 10
    
    await state.update_data(attempts=attempts)
    
    if user_guess < secret_number:
        await message.answer(f'Попытка {attempts}. Загаданное число больше!')
        
    elif user_guess > secret_number:
        await state.update_data(attempts=attempts)
        await message.answer(f'Попытка {attempts}. Загаданное число меньше!')
        
    else:
        await message.answer(f'Поздравляю! Ты угадал(а) число {secret_number} за {attempts} попыток!')
        await state.clear()
        return

    if attempts >= max_attempts and user_guess != secret_number:
        await message.answer(f'Попытки закончились! Я загадал число {secret_number}. Попробуй еще раз: /game')
        await state.clear()
        return

class RPSStates(StatesGroup):
    waiting_for_move = State() #ожидание хода игрока
    
@router.message(Command('suyefa'))
async def rps_start(message: types.Message, state: FSMContext):
    await message.answer('Игра "Камень, ножницы, бумага" началась!', reply_markup=rps_keyboard())
    await state.update_data(user_score=0, bot_score=0)
    await state.set_state(RPSStates.waiting_for_move)
    
@router.message(StateFilter(RPSStates.waiting_for_move))
async def rps_process(message: types.Message, state: FSMContext):
    user_choice = message.text #берем только слово без смайлика
    choices = ['Камень🪨', 'Ножницы✂️', 'Бумага📄']
    
    if user_choice == 'Стоп❌':
        data = await state.get_data()
        await message.answer(f'Игра окончена! Финальный счет: Вы {data['user_score']} : {data['bot_score']} Бот', reply_markup=types.ReplyKeyboardRemove())
        await state.clear()
        return
    
    if user_choice not in choices:
        await message.answer('Пожалуйста, выбери вариант на кнопках!')
        return
    
    bot_choice = random.choice(choices)
    data = await state.get_data()
    user_score = data['user_score']
    bot_score = data['bot_score']
    
    #логика победы
    if user_choice == bot_choice:
        result = 'Ничья!🤝'
    elif (user_choice.split()[0] == 'Камень🪨' and bot_choice == 'Ножницы✂️') or \
        (user_choice.split()[0] == 'Ножницы✂️' and bot_choice == 'Бумага📄') or \
        (user_choice.split()[0] == 'Бумага📄' and bot_choice == 'Камень🪨'):
            result = 'Вы победили!🏆'
            user_score += 1
    else:
        result = 'Бот победил!🤖'
        bot_score += 1
    
    await state.update_data(user_score=user_score, bot_score=bot_score)
    await message.answer(f'Ваш ход: {user_choice}\nХод бота: {bot_choice}\n\n{result}\nСчет: Вы {user_score} : {bot_score} Бот', reply_markup=rps_keyboard())


async def main():
    bot = Bot(token=TOKEN)
    print('Start...')
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())