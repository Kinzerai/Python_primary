# Показать четные числа от 1 о N

# -*- coding: utf-8 -*-

a = int(input('Введите целое число:'))

for i in range(1, a+1):
    if not i % 2:
        print(i)


  