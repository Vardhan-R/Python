import numpy as np

n = 3

a = np.array([[2, 3, 4],
              [4, 5, 7],
              [-6, 12, 27]])

b = np.array([[3, -4, -3]])

aug = np.concatenate((a, b.T), axis=1, dtype="float64")

for i in range(n - 1):
    aug[i] /= aug[i][i]
    for j in range(i + 1, n):
        aug[j] -= aug[j][i] * aug[i]
aug[-1] /= aug[-1][-2]

for i in range(n - 1, 0, -1):
    for j in range(i - 1, -1, -1):
        aug[j] -= aug[j][i] * aug[i]

x = aug[:, -1]
print(x)