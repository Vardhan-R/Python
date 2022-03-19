import math, pygame, random, time

l = []
for i in range(3):
    l.append([])
    for j in range(16):
        if not(j % 2 ** (2 - i)):
            l[i].append(random.randint(0, 100 / 2 ** i))
print(l)

# [10, 20, 30, 40]
# [5, 10, 15, 20, 25, 30, 35, 40]
# [2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20, 22.5, 25, 27.5, 30, 32.5, 35, 37.5, 40]