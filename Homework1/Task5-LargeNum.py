# 5. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа.


from ast import Num
import random

numA = random.randint(10,100)
print(numA)
numB = numA // 10
numC = numA % 10

if numB > numC:
    print(f'{numB} is the largest digit of number {numA}')
if numB < numC:
    print(f'{numC} is the largest digit of number {numA}')
if numB == numC:
    print(f'{numB} equals {numC}')