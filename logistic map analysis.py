import math, pygame, random, time

r = 3.7
density = 100
lst = []

def func(f, n):
    return round(f * n * (1 - n), math.ceil(math.log10(density)))

for i in range(density):
    lst.append([])
    z = i / density
    while z not in lst[-1]:
        lst[-1].append(z)
        z = func(r, z)
    lst[-1].append(z)
    z = lst[-1][0]
    while lst[-1][0] != lst[-1][-1]: lst[-1].pop(0)

for i in range(len(lst)):
    print(i / density, lst[i])