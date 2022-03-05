# Найти третью цифру числа или сообщить, что её нет
a = input('Введите число:')
print(a[2])
if int(a) < 0:
    a = str(int(a)*-1)
if a > 0:
    if len(a) < 3:
        print('Мало')
    else:
        print(a[2])