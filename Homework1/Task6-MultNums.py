# Выяснить, кратно ли число заданному, если нет, вывести остаток.


import random

a = random.randint(2,50)
b = random.randint(2,15)
print(f'a = {a}, b = {b}')
if a % b == 0:
    print(f'{a} is multiple of {b}')
if a % b != 0:
    print (f'{a} is not multiple of {b}, remainder is {a % b}')