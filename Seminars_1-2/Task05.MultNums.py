# Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

import random

a = random.randint(5,99)

print(f'a = {a}')


if a % 5 == 0 and a % 10 == 0:
    print(f'{a} is multiple of 5 and 10')
else:
    print (f'{a} is NOT multiple of 5 and 10')

if a % 15 == 0 and a % 30 != 0:
    print(f'{a} is multiple of 15 not of 30')



