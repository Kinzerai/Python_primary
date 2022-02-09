# Показать числа от -N о N

import random

a = random.randint(-10,0)
b = random.randint(0,10)

print(f'-N = {a}, N = {b}')

for i in range(a, b+1):
    print(i)
    
