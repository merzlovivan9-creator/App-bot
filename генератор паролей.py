import random
import time

a = "abcdefghijklmnopqrstuvwxyz"
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c = "0123456789"
d = "@!$#*^%/+-_[]{},."

all = a + b + c + d
length = int(input('Введите длинну пароля(0-79): '))
password = "".join(random.sample(all,length))
print('Идет генерация пароля...')
time.sleep(3)
print('Ваш пароль: ', password)