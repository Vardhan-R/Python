x = [1, 2, 3, 4, 5]
y = [1, 3, 6, 9, 14]

n = 1
l = len(x)
sx = [] # s ==> sum
sxy = []

def det(t):
    if len(t) == len(t[0]):
        if len(t) > 2:
            s = 0
            for m in range(len(t)):
                p = []
                for n in t:
                    p.append(n.copy())
                p.pop(0)
                for n in range(len(p)):
                    p[n].pop(m)
                s += (-1) ** m * t[0][m] * det(p)
            return s
        elif len(t) == 2: return t[0][0] * t[1][1] - t[0][1] * t[1][0]
        elif len(t) == 1: return t[0][0]
        else: return 0

def mAdd(a, b):
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        sum_matrix = []
    for m in range(len(a)):
        sum_matrix.append([])
    for m in range(len(a)):
        for n in range(len(a[0])):
            sum_matrix[m].append(a[m][n] + b[m][n])
    return sum_matrix

def mSub(a, b):
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        diff_matrix = []
    for m in range(len(a)):
        diff_matrix.append([])
    for m in range(len(a)):
        for n in range(len(a[0])):
            diff_matrix[m].append(a[m][n] + b[m][n])
    return diff_matrix

def mMult(a, b):
    if len(a[0]) == len(b):
        prod_matrix = []
        temp_matrix = []
        for m in range(len(b[0])):
            temp_matrix.append(0)
        for m in range(len(a)):
            prod_matrix.append(temp_matrix.copy())
        for m in range(len(a)):
            for n in range(len(b[0])):
                for o in range(len(b)):
                    prod_matrix[m][n] += a[m][o] * b[o][n]
        return prod_matrix

def mSMult(k, a):
    new_matrix = a.copy()
    for m in range(len(a)):
        for n in range(len(a[0])):
            new_matrix[m][n] *= k
    return new_matrix

def mMinor(a, r, c):
    temp_matrix = []
    for m in range(len(a)):
        temp_matrix.append([])
        for n in range(len(a[m])):
            temp_matrix[m].append(a[m][n])
    temp_matrix.pop(r - 1)
    for m in range(len(temp_matrix)):
        temp_matrix[m].pop(c - 1)
    return det(temp_matrix)

def mCofactor(a, r, c):
    return (-1) ** (r + c) * mMinor(a, r, c)

def mTranspose(a):
    temp_matrix = []
    for m in range(len(a[0])):
        temp_matrix.append([])
    for m in range(len(a)):
        for n in range(len(a[0])):
            temp_matrix[n].append(a[m][n])
    return temp_matrix

def mAdj(a):
    cofactor_matrix = []
    for m in range(len(a)):
        cofactor_matrix.append([])
    for p in range(len(a)):
        for q in range(len(a[0])):
            cofactor_matrix[p].append(mCofactor(a, p + 1, q + 1))
    return mTranspose(cofactor_matrix)

def mInv(a):
    if len(a) == len(a[0]):
        return mSMult(1 / det(a), mAdj(a))

temp = []
for i in range(n + 1):
    temp.append(0)
for i in range(n + 1):
    sx.append(temp.copy())
    sxy.append([0])

for i in range(n + 1):
    for j in range(n + 1):
        for k in x:
            sx[i][j] += k ** (i + j)

for i in range(n + 1):
    for j in range(l):
        sxy[i][0] += x[j] ** i * y[j]

sxi = mInv(sx) # i ==> inverse

coeffs = mMult(sxi, sxy)
print(coeffs)

def func(x_input):
    y_c = 0 # c ==> calc
    for m in range(n + 1):
        y_c += coeffs[m][0] * x_input ** m
    return y_c

y_calc = []

for i in x:
    y_calc.append(func(i))

error = 0
for i in range(l):
    error += (y_calc[i] - y[i]) ** 2
print(error)