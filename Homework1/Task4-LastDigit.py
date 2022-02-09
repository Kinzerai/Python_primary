# 4. Показать последнюю цифру трёхзначного числа.

def lastdigit (num):
    num = num % 100 % 10
    return num

number = int(input('Enter 3-digit number: '))

print(f'Third digit of {number} is {lastdigit(number)}')


# Без функции:
# from ast import Num
# import random

# numA = random.randint(100,1000)
# print(numA)
# numB = numA % 100 % 10
# print(numB)