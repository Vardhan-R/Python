import math, matplotlib.pyplot as plt

x = []
p = []

def walk(n):
    temp = []
    tri = [1, 1]
    origin = []

    for i in range(n):
        temp.append(1)
        for j in range(len(tri) - 1):
            temp.append(tri[j] + tri[j + 1])
        temp.append(1)

        if len(temp) % 2:
            origin.append(temp[math.floor(len(temp) / 2)])
            temp[math.floor(len(temp) / 2)] = 0

        tri = temp.copy()
        temp.clear()

    return sum(origin[i] / 4 ** (i + 1) for i in range(len(origin)))

for i in range(2, 101, 2):
    x.append(i)
    p.append(walk(i))

plt.plot(x, p)
plt.show()
