# найти максимальное из 2-ух чисел

a = int(input('Введите первое целое число:'))
b = int(input('Введите первое целое число:'))

if a > b:
    print(f'{a} максимальное, {b} минимальное')

elif a < b:
    print(f'{b} максимальное, {a} минимальное')
    
else:
    print(f'{b} равно {a} ') 


def my_max(a,b):
    if a > b:
        print(f'{a} максимальное, {b} минимальное')
        return a
    elif a < b:
        print(f'{b} максимальное, {a} минимальное')
        return b
    else:
        print(f'{b} равно {a} ') 
        return a, b

my_max(a,b)
num = my_max
print(num)
print(type(num))    
 


   
