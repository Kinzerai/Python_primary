# 10. Найти расстояние между двумя точками пространства

import math
import random

a = random.randint(-10,10)
b = random.randint(-10,10)
c = random.randint(-10,10)
d = random.randint(-10,10)

Point1 = [a, b]
Point2 = [c, d]

print(f'First point: {Point1}')
print(f'Second point: {Point2}')

distance = round((math.sqrt( (Point1[0]-Point2[0])**2+(Point1[1]-Point2[1])**2)),2) 
print(f'Distance between 2 points is {distance}')


# distance2 = round ((math.sqrt( (a-c)**2 + (b-d)**2)),2) # 2-ой вариант 
# print(distance2)