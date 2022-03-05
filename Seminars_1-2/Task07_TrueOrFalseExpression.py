# # 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# # для всех значений предикат

def statement_truth(a,b,c):
    if (not (a or b or c)) == ((not a) and (not b) and (not c)):
        print(f'True for: x = {a}, y = {b}, z = {c}')
        result = True
    else:
        result = False
        print(result)


x = True
y = True
z = True
statement_truth(x,y,z)

x = True
y = False
z = True
statement_truth(x,y,z)

x = True
y = True
z = False
statement_truth(x,y,z)

x = False
y = True
z = True
statement_truth(x,y,z)

x = False
y = False
z = True
statement_truth(x,y,z)
  
x = False
y = True
z = False
statement_truth(x,y,z)
   
x = True
y = False
z = False
statement_truth(x,y,z)
   
x = False
y = False
z = False
statement_truth(x,y,z)





# Альтернатива без метода:
# from operator import truediv
# from turtle import clear


# x = True
# y = True
# z = True

# result = True

# if (not (x or y or z)) == ((not x) and (not y) and (not z)):
#     print(f'True for: x = {x}, y = {y}, z = {z}')
# else:
#     result = False
#     print(result)

# x = True
# y = False
# z = True

# if (not (x or y or z)) == ((not x) and (not y) and (not z)):
#     print(f'True for: x = {x}, y = {y}, z = {z}')
# else:
#     result = False
#     print(result)

# x = True
# y = True
# z = False

# if (not (x or y or z)) == ((not x) and (not y) and (not z)):
#     print(f'True for: x = {x}, y = {y}, z = {z}')
# else:
#     result = False
#     print(result)

# x = False
# y = True
# z = True

# if (not (x or y or z)) == ((not x) and (not y) and (not z)):
#     print(f'True for: x = {x}, y = {y}, z = {z}')
# else:
#     result = False
#     print(result)

# x = False
# y = False
# z = True

# if (not (x or y or z)) == ((not x) and (not y) and (not z)):
#     print(f'True for: x = {x}, y = {y}, z = {z}')
# else:
#     result = False
#     print(result)    

# x = False
# y = True
# z = False

# if (not (x or y or z)) == ((not x) and (not y) and (not z)):
#     print(f'True for: x = {x}, y = {y}, z = {z}')
# else:
#     result = False
#     print(result)    

# x = True
# y = False
# z = False

# if (not (x or y or z)) == ((not x) and (not y) and (not z)):
#     print(f'True for: x = {x}, y = {y}, z = {z}')
# else:
#     result = False
#     print(result)    

# x = False
# y = False
# z = False

# if (not (x or y or z)) == ((not x) and (not y) and (not z)):
#     print(f'True for: x = {x}, y = {y}, z = {z}')
# else:
#     result = False
#     print(result)   