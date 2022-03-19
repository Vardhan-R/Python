import math, pygame, random, time

n = 1000
my_quarter_pi = 0

for i in range(n): # f(n)
    my_quarter_pi += (-1) ** i / (2 * i + 1)

my_quarter_pi += (-1) ** n / (2 * (2 * n + 1)) # (f(n) + f(n + 1)) / 2

print(4 * my_quarter_pi)