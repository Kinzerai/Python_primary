# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат

from operator import truediv
from turtle import clear


x = True
y = True
z = True

result = True

if (not (x or y or z)) == ((not x) and (not y) and (not z)):
    print(f'True for: x = {x}, y = {y}, z = {z}')
else:
    result = False
    print(result)

x = True
y = False
z = True

if (not (x or y or z)) == ((not x) and (not y) and (not z)):
    print(f'True for: x = {x}, y = {y}, z = {z}')
else:
    result = False
    print(result)

x = True
y = True
z = False

if (not (x or y or z)) == ((not x) and (not y) and (not z)):
    print(f'True for: x = {x}, y = {y}, z = {z}')
else:
    result = False
    print(result)

x = False
y = True
z = True

if (not (x or y or z)) == ((not x) and (not y) and (not z)):
    print(f'True for: x = {x}, y = {y}, z = {z}')
else:
    result = False
    print(result)

x = False
y = False
z = True

if (not (x or y or z)) == ((not x) and (not y) and (not z)):
    print(f'True for: x = {x}, y = {y}, z = {z}')
else:
    result = False
    print(result)    

x = False
y = True
z = False

if (not (x or y or z)) == ((not x) and (not y) and (not z)):
    print(f'True for: x = {x}, y = {y}, z = {z}')
else:
    result = False
    print(result)    

x = True
y = False
z = False

if (not (x or y or z)) == ((not x) and (not y) and (not z)):
    print(f'True for: x = {x}, y = {y}, z = {z}')
else:
    result = False
    print(result)    

x = False
y = False
z = False

if (not (x or y or z)) == ((not x) and (not y) and (not z)):
    print(f'True for: x = {x}, y = {y}, z = {z}')
else:
    result = False
    print(result)   