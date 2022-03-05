# Указав номер четверти прямоугольной системы координат, 
# показать допустимые значения координат для точек этой четверти

plane = int(input('Please enter coordinate plane number: '))

if ( plane > 4 or plane < 1):
    print('Coordinate plane number is incorrect. Please enter digit from 1 to 4 ')

if plane == 1:
    print(f'In {plane} plane there are coordinates: x > 0 и y > 0')
if plane == 2:
    print (f'In {plane} plane there are coordinates: x < 0 и y > 0')
if plane == 3:
    print (f'In {plane} plane there are coordinates: x < 0 и y < 0')
if plane == 4:
    print (f'In {plane} plane there are coordinates:x > 0 и y < 0')