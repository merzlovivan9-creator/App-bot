import random

def guess_the_number():
    secret_number = random.randint(1,100)
    attempts = 0
    max_attempts = 10

    print("Добро пожаловать в игру 'Угадай число'!")
    print(f"Я загадал число от 1 до 100. У вас {max_attempts} попыток.")

    while attempts < max_attempts:
    # Получаем предположение игрока
        try:
            guess = int(input(f"Попытка {attempts + 1}. Ваше предположение: "))
        except ValueError:
            print("Пожалуйста, введите целое число.")
            continue

        attempts += 1

        # Проверяем предположение
        if guess < secret_number:
            print("Загаданное число больше.")
        elif guess > secret_number:
            print("Загаданное число меньше.")
        else:
            print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток!")
            break
    if attempts >= max_attempts and guess != secret_number:
        print(f"К сожалению, попытки закончились. Загаданное число было: {secret_number}")

# Запускаем игру
guess_the_number()