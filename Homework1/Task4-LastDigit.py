# 4. Показать последнюю цифру трёхзначного числа.

from ast import Num
import random

numA = random.randint(100,1000)
print(numA)
numB = numA % 100 % 10
print(numB)