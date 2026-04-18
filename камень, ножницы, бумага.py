import random

start = input('Вы запустили игру "камень, ножницы, бумага", желаете продолжить, или закрыть игру? (введите "+" чтобы продолжить, или "-" чтобы закрыть игру) ')

if start == '+':
    print('Загрузка...')
    print('Игра началась!')
    print('Если захотите закончить, введите "-".')
    print('Если хотите узнать счет, введите "с".')
    user_ball = 0
    rand_ball = 0
    user_rand = 0
    while True:
        user = input('Камень, ножницы или бумага? (введите к, н или б): ')
        list_play = ("к", "н", "б")
        if user in list_play:
            rand = random.choice(list_play)
            print(rand)
            
            if rand == 'к' and user == 'н':
                rand_ball += 1
                print('Ты проиграл.')
            if rand == 'к' and user == 'б':
                user_ball += 1
                print('Молодец! Ты выиграл!')
            if rand == 'к' and user == 'к':
                user_rand += 1
                print('Ничья!')
            if rand == 'н' and user == 'к':
                user_ball += 1
                print('Ты победил, молодец!')
            if rand == 'н' and user == 'б':
                rand_ball += 1
                print('Ты проиграл.')
            if rand == 'н' and user == 'н':
                user_rand += 1
                print('Ничья!')
            if rand == 'б' and user == 'н':
                user_ball += 1
                print('Ты победил!')
            if rand == 'б' and user == 'к':
                rand_ball += 1
                print('Ты проиграл.')
            if rand == 'б' and user == 'б':
                user_rand += 1
                print('Ничья!')
        elif user == "с":
            print('Ваши баллы:', user_ball, 'Баллы вашего соперника:', rand_ball, 'Ничья:', user_rand)
        elif user == "-":
            if user_ball == 0 and rand_ball == 0:
                print('Игра окончена. Заходите еще!')
            elif user_ball > 0 and rand_ball > 0:
                print('Ваши баллы: ', user_ball, 'Баллы вашего соперника: ', rand_ball)
                print('Игра окончена. Заходите еще!')
            break
        else:
            print('Введите к, н или б!')
            
elif start == "-":
    print('Жаль... Игра окончена :(')
else:
    print('Простите, я вас не понял, если хотите играть перезапустите программу и введите "+".')