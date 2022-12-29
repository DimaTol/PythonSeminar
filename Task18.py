# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.


import random

n = int(input("Задайте длинну массива: "))
l = []
for num in range(0, n):
    random_number = round(random.randint(0, 10))
    l.append(random_number)
print(l)


x = int(input("Введите число X которое надо проверить: "))


def checkNumber(count):
    for i in range(0, len(l)):
        if l[i] == x+count:
            return l[i]
        elif l[i] == x-count:
            return l[i]

    return checkNumber(count+1)

print(checkNumber(0))