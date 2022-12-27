# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2


from random import randint

coin = int (input ("Сколько монеток лежат на столе: "))

list_coin = []

count_1 = 0
count_2 = 0

for i in range (coin):
    random_num = randint (0,1) # 0 - орел, 1 - решка
    list_coin.append(random_num)
    if list_coin [i] == 0: count_1+=1 
    if list_coin [i] == 1: count_2+=1
    
print (list_coin)
    
if count_1 > count_2:
    for n in range (coin):
        if list_coin [n] == 1: 
           list_coin [n] = 0
            
if count_1 < count_2:
    for k in range (coin):
        if list_coin [k] == 0: 
           list_coin [k] = 1 

min = 0
if count_1 < count_2: min = count_1
else:
    min = count_2

print (f"Монеток с Решкой {count_1}, Монеток с Орлом {count_2}")
print (f"Необходимо перевернуть {min} монеток")
