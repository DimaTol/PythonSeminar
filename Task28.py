# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых 
# неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

a = int (input('Введите число А: '))
b = int (input ('Введите число B: '))

def sum(x, y):
    if y==0:
        return x
    else:
        if x > 0 and y > 0:
            return sum(x+1,y-1)

print(sum(a, b))
    