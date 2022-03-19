import matplotlib.pyplot as plt, numpy as np, math, random, time

data_x = []
data_y = []
# data_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# data_y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# for i in range(10):
#     data_x.append(random.randint(0, 10))
#     data_y.append(random.randint(0, 10))

# semicircle
d = 50
for i in range(-d, d):
    data_x.append(i / d)
    data_y.append(math.sqrt(1 - (i / d) ** 2))

m = 0
b = 0
epochs = 1000
l = 0.01

# def sign(x):
#     if x == 0: return 0
#     else: return (x / abs(x))

def calcError(x_exp, y_exp, m, b):
    error = 0
    n = len(x_exp)
    for i in range(n):
        error += (y_exp[i] - (m * x_exp[i] + b)) ** 2
    return error / n

def diff(x_exp, y_exp, m, b):
    dE_m = 0
    dE_b = 0
    n = len(x_exp)
    for i in range(n):
        dE_m += -2 * x_exp[i] * (y_exp[i] - (m * x_exp[i] + b))
        dE_b += -2 * (y_exp[i] - (m * x_exp[i] + b))
    # print(dE_m / n, dE_b / n)
    m -= l * dE_m / n
    b -= l * dE_b / n
    return m, b

for i in range(epochs):
    m, b = diff(data_x, data_y, m, b)

x = np.array(data_x)
y = m * x + b
plt.scatter(data_x, data_y)
plt.plot(x, y)
print(calcError(data_x, data_y, m, b))

plt.show()