a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))

while True:
    action = input('Введите действие(+ - / *): ')
    result = 0
    if action == '+':
        result = a + b
    elif action == '-':
        result = a - b
    elif action == '/':
        result = a / b
    elif action == '*':
        result = a * b
    else:
        print('ERROR!, Вы ввели неправильное действие!')
        continue   

    print(result)
    break