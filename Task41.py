# Вычислить значение выражения:
# 12 + 15
# 12 / 15
# 112 * 15

# 1. Где операторы?
# 2. Где числовые значения?
# Уровень 1:

# - 1 действие
# - 2 аргумента

# Уровень 2:
# - Количество действие произвольное
# 12 + 15 - 4

# Уровень 3:
# - Действия имеют приоритет
# 12 - 4*2

# Уровень 4:
# - Действия разделяются скобками
# (12 - 4) * 2

# n = '12+5'
# m = n.split()
# m2 = []

# def calc (a,b,c):
#     if c == '+':
#         return(a + b)
#     elif c == '-':
#         return(a - b)
#     elif c == '/':
#          return(a / b)
#     elif c == '*':
#         return(a * b)
    
# a = int(m[0])
# c = m[1], m [3], m [4]
# b = int(m[2])

# result = int(m[0])

# for i in range(1, len(m) - 1, 2):
#     if m[i] == '*' or m[i] == '/':
#         result = calc(int(m[i - 1]), int(m[i + 1]), m[i])
#     m2.append(result)
# else:
#     m2.append(m[i])
#     m2.append(int(m[i + 1]))

# print (n)
# print (m)
# print(m2)
# print(result)


# Уровень 1
# n = '12 + 5'
# m = n.split()

# a = int(m[0])
# c = m[1]
# b = int(m[2])

# def calc (a,b,c):
#     if c == '+':
#         return(a + b)
#     elif c == '-':
#         return(a - b)
#     elif c == '/':
#          return(a / b)
#     elif c == '*':
#         return(a * b)
    
# result = calc (a,b,c)
# print (result)

# Уровень №2
# - Количество действие произвольное
# 12 + 15 - 4

# n = '12 + 5 - 4'
# m = n.split()

# a = int(m[0])
# c = m[1]
# b = int(m[2])

# m2 = []
# def calc (a,b,c):
#     if c == '+':
#         return(a + b)
#     elif c == '-':
#         return(a - b)
#     elif c == '/':
#          return(a / b)
#     elif c == '*':
#         return(a * b)
    
# result = int (m[0])

# for i in range(1,len(m) - 1,2):
#     result = calc (result, int (m[i+1]),m[i])
# print (result)


# Уровень 3:
# - Действия имеют приоритет
# 12 - 4*2
n = '12 - 4 * 2 + 6 / 3'
m = n.split()
m2 = []

if m[0].isdigit():
    m.insert(0, '+')
    
result = 0

for i in range(0, len(m) - 1, 2):
    if m[i] == '*':
        multyply = int(m2[-1]) * int(m[i + 1])
        m2[-1] = multyply
    elif m[i] == '/':
        division = int(m2[-1]) / int(m[i + 1])
        m2[-1] = division
    else:
        m2.append(m[i])
        m2.append(m[i + 1])

for i in range(0, len(m2) -1, 2):
    if m2[i] == '+':
        result += int(m2[i+1])
    elif m[i] == '-':
        result -= int(m2[i+1])
    else:
        continue
print(result)
    