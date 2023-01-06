# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.
# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)
# Output: 11 6
# 6 12

import random

n = int(input("Введите кол-во эл-тов первого набора: "))
l = []
for num in range(0, n):
    random_number = round(random.randint(0, 10))
    l.append(random_number)
l = (sorted(l))
print(l)

m = int(input("Введите кол-во эл-тов второго набора: "))
x = []
for num in range(0, m):
    random_number = round(random.randint(0, 10))
    x.append(random_number)
x = (sorted(x))
print(x)

l = set(l)

res = []
for item in l:
    if item in x:
        res.append(item)
if len(res)!=0:
    print ('совпадения следующие', res)
else:
    print ('нет совпадений')




