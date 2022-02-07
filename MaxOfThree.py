# max из 3-х

import random

a = random.randint(1,10)
b = random.randint(1,15)
c = random.randint(1,20)


max = a

if max < b:
    max = b
if max < c:
    max = c

print(f'Максимальное число из пяти случайных чисел {a},{b},{c}: {max}')

