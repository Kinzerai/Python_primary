# 2. По заданному номеру дня недели вывести его название


weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

dayNo = int(input("Введите номер дня недели от 1 до 7: "))
if dayNo == 1:
    print(weekdays[0])
if dayNo == 2:
    print(weekdays[1])
if dayNo == 3:
    print(weekdays[2])
if dayNo == 4:
    print(weekdays[3])
if dayNo == 5:
    print(weekdays[4])
if dayNo == 6:
    print(weekdays[5])    
if dayNo == 7:
    print(weekdays[6])
if dayNo > 7 or dayNo < 1:
    print('Неверно введено значение!')