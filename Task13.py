# Задача №13
# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. 
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель.
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50

# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

import random 
n = int (input ("введите колличество дней: "))
m = []
count = 0
max = 0
for i in range (0,n):
    random_num = round (random.randint (-50,50),0)
    m.append (random_num)
    if m[i] < 0 : count = 0
    if m[i] > 0:
        count +=1
        if max < count: max = count
        
# print (n)
print (m)
print (count)
print(max)


# from random import randint


# days = int(input('Введите количество рассматриваемых дней: '))

# temp = []
# long = []

# for t in range(days):
#     num = round(randint(-50, 51))
#     temp.append(num)

# print(temp)

# count = 0
# for i in temp:

#     if i > 0:
#         count = count + 1
#     elif i <= 0:
#         long.append(count)
#         count = 0
# long.append(count)

# max=long[0]

# for findMax in long:
#   if findMax > max:
#      max = findMax
  
# print(long)
# print(max)