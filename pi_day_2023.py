import math, random

n = 10 ** 7
c = 0
height = 100000

for i in range(n):
    y = random.randrange(0, height * 10 ** 6) / 10 ** 6
    c += math.floor(y + math.sin(random.randrange(0, round(math.pi * 10 ** 6)) / 10 ** 6)) - math.floor(y)
    if i % 10 ** 6 == 0:
        print(i)

print(2 * n / c)