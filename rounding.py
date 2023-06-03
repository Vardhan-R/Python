import numpy as np

a = 100010
b = 999990
op = 1

def nMin(n):
    n_0 = n
    i = -1
    while not(n % 10):
        n //= 10
        i += 1
    return n_0 - 5 * 10 ** i

def nMax(n):
    n_0 = n
    i = -1
    while not(n % 10):
        n //= 10
        i += 1
    return n_0 + 5 * 10 ** i

def operate(a, b, n):
    if n == 1:
        return a + b
    if n == 2:
        return a - b
    if n == 3:
        return a * b
    return a / b

a_min = nMin(a)
a_max = nMax(a)
b_min = nMin(b)
b_max = nMax(b)
c = operate(a, b, op)
c_min = operate(a_min, b_min, op)
c_max = operate(a_max, b_max, op)

# rng = np.random.default_rng()
# arr = np.array([7000, 65000, 694800, 3800, 6909, 6905, 295040])
# for i in arr:
#     print(f"{nMin(i)}, {i}, {nMax(i)}")

print("Actual:", c)
print("Min:", c_min)
print("Max:", c_max)
print("Error:", (c_max - c_min) / 2)

i = 0
while round(c_min, i) == round(c_max, i):
    i += 1
print(i)