
def arbuzLine(N):
    arbuzes=[]
for _ in range(N):
    arbuzes.append(random.randint(5000,30000))
    arbuzes.sort()
print(arbuzes)

min=max=arbuzes[0]
for item in arbuzes:
    if min>item: min = item
    elif max < item: max = item
    return arbuzes [0]

n = int (input ("введите колличество дней: "))
print (arbuzLine (N))