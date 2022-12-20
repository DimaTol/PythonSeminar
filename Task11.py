# Задача №11
# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.

n = int (input ("введите число"))

def fibonache (n):
    if n == 1:
        return 2,3
    number0 = 0
    number1 = 1
    count = 2
    while n >= number1:
        if n == number1:
            return count
        temp = number1
        number1 += number0
        number0 = temp
        count += 1
    return -1

print (fibonache(n))