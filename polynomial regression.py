import math, matplotlib.pyplot as plt, numpy as np, random

data_x = []
data_y = []

# random pts
data_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(10):
    data_y.append(random.randint(0, 10))

# semicircle
# d = 50
# for i in range(-d, d):
#     data_x.append(i / d)
#     data_y.append(math.sqrt(1 - (i / d) ** 2))

# sine wave
# d = 20
# lb = -4 * d
# ub = 4 * d
# for i in range(lb, ub):
#     data_x.append(i / d)
#     data_y.append(math.sin(i / d))

# cosine wave
# d = 20
# lb = -4 * d
# ub = 4 * d
# for i in range(lb, ub):
#     data_x.append(i / d)
#     data_y.append(math.cos(i / d))

n = 1
coeffs = []
for i in range(n + 1):
    coeffs.append(0)
epochs = 1000
l = 0.01

def calcError(x_exp, y_exp, coeffs):
    error = 0
    n = len(x_exp)
    for i in range(n):
        error += (y_exp[i] - eq(coeffs, x_exp[i])) ** 2
    return error / n

def eq(coeffs, x):
    y = 0
    for i in range(len(coeffs)):
        y += coeffs[i] * x ** i
    return y

def diff(x_exp, y_exp, coeffs):
    dE = []
    for i in range(len(coeffs)): dE.append(0)
    n = len(x_exp)
    for i in range(len(coeffs)):
        for j in range(n):
            dE[i] += -2 * (y_exp[j] - eq(coeffs, x_exp[j])) * x_exp[j] ** i
        coeffs[i] -= l * dE[i] / n
    return coeffs

for i in range(epochs):
    coeffs = diff(data_x, data_y, coeffs)

x = np.array(data_x)
y = eq(coeffs, x)
plt.scatter(data_x, data_y)
plt.plot(x, y)
coeffs.reverse()
print(calcError(data_x, data_y, coeffs), coeffs)

plt.show()