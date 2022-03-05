# 4. Показать первую цифру дробной части числа


num = float(input('Введите дробное число: '))
print(num)

def num2 (x):
    return int (x * 10 % 10)

print(num2(num))