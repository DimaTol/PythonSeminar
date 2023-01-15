# Напишите функцию same_by(characteristic, objects), которая проверяет, 
# все ли объекты имеют одинаковое значение некоторой характеристики, 
# и возвращают True, если это так. Если значение характеристики для разных объектов отличается 
# - то False. Для пустого набора объектов, функция должна возвращать True. 
# Аргумент characteristic - это функция, которая принимает объект и вычисляет 
# его характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same


    
values = [0, 2, 10, 6]

def same_by(func, val):
    return len(set([func(el) for el in val])) == 1

if same_by (lambda x:x %2,values):
    print ("same")
else:
    print ("different")
    

