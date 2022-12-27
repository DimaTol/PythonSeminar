<<<<<<< HEAD

def arbuzLine(N):
    arbuzes=[]
for _ in range(N):
=======
# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

N = int (input ())
def arbuzLine(N):
    arbuzes= []
for i in range(N):
>>>>>>> 47efdfcf28b9ea7965d25031e62f6db9265e05e0
    arbuzes.append(random.randint(5000,30000))
    arbuzes.sort()
print(arbuzes)

min=max=arbuzes[0]
<<<<<<< HEAD
for item in arbuzes:
    if min>item: min = item
    elif max < item: max = item
    return arbuzes [0]

n = int (input ("введите колличество дней: "))
print (arbuzLine (N))
=======
for n in arbuzes:
    if min>n: min = n
    elif max < n: max = n

return min, max

    # return arbuzes[0],arbuzes[-1]  
print arbuzLine (N)
>>>>>>> 47efdfcf28b9ea7965d25031e62f6db9265e05e0
