from built_modules import import_matrices as mat
from math import *

n = 1000
t = pi / (2 * n)
r_x = [[1, 0, 0],
       [0, cos(t), sin(t)],
       [0, -sin(t), cos(t)]]
r_y = [[cos(t), 0, sin(t)],
       [0, 1, 0],
       [-sin(t), 0, cos(t)]]
a = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]

for i in range(n):
    a = mat.mult(r_x, a)
    a = mat.mult(r_y, a)
    # print(i)

for i in range(3):
    for j in range(3):
        a[i][j] = round(a[i][j], 5)

for i in a:
    print(i)