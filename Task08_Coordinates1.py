# Сообщить в какой четверти координатной плоскости или 
# на какой оси находится точка с координатами Х и У 

import random

x = random.randint(-10,10)
y = random.randint(-10,10)


if x > 0 and y > 0:
    print(f'Point ({x} , {y}) is located in 1 Quadrant of Coordinate Plane')

if x < 0 and y > 0:
    print(f'Point ({x} , {y}) is located  in 2 Quadrant of Coordinate Plane')

if x < 0 and y < 0:
    print(f'Point ({x} , {y}) is located  in 3 Quadrant of Coordinate Plane')

if x > 0 and y < 0:
    print(f'Point ({x} , {y}) is located in 4 Quadrant of Coordinate Plane')

if x == 0 and y != 0:
    print(f'Point ({x} , {y}) is located  on Y axis')

if x != 0 and y == 0:
    print(f'Point ({x} , {y}) is located  on X axis')

if x == 0 and y == 0:
    print(f'Point ({x} , {y}) is located  in the center of axes')