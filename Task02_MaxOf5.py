# Найти максимальное из пяти чисел
#from turtle import clear
import random

a = random.randint(1,10)
b = random.randint(1,15)
c = random.randint(1,20)
d = random.randint(1,10)
e = random.randint(1,15)

max = a

if max < b:
    max = b
if max < c:
    max = c
elif max < d:
    max = d
if max < e:
    max = e
print(f'Максимальное число из пяти случайных чисел {a},{b},{c},{d},{e}: {max}')

