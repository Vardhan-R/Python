import import_number_system_converter as nsc, matplotlib.pyplot as plt

n = 16
a = 2 ** n
ranges_lst = []

for i in range(a):
    b = nsc.convertNum(i, 10, 2, n)
    x = 0
    x_max = 0
    x_min = 0
    for j in b:
        x += 2 * int(j) - 1
        x_max = max(x, x_max)
        x_min = min(x, x_min)
    ranges_lst.append(x_max - x_min)
print(sum(ranges_lst) / len(ranges_lst))

freq = [0 for i in range(n + 1)]

for i in ranges_lst:
    freq[i] += 1

plt.bar([i for i in range(n + 1)], freq)
plt.show()
