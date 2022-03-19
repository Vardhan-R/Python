import math

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

class Vector:
    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def mult(self, a):
        return Vector(a * self.x, a * self.y, a * self.z)

    def mag(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def magSq(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def normalise(self):
        if self.mag() != 0:
            return self.mult(1 / self.mag())

    def setMag(self, m):
        return Vector(self.x / self.mag(), self.y / self.mag(), self.z / self.mag()).mult(m)

    def dir(self): # z = 0
        return(math.atan2(self.y, self.x))

    def setDir(self, t): # z = 0
        return Vector(self.mag() * math.cos(t), self.mag() * math.sin(t), self.z)

    def rotate(self, t): # z = 0
        return Vector(self.mag() * math.cos(self.dir() + t), self.mag() * math.sin(self.dir() + t), self.z)

def vectorAdd(a, b):
    return Vector(a.x + b.x, a.y + b.y, a.z + b.z)

def vectorSub(a, b):
    return Vector(a.x - b.x, a.y - b.y, a.z - b.z)

def vectorDot(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z

def vectorCross(a, b):
    return Vector(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x)

def vectorDistBetween(a, b):
    return Vector(a.x - b.x, a.y - b.y, a.z - b.z).mag()

def vectorAngBetween(a, b):
    return math.acos(vectorDot(a, b) / (a.mag() * b.mag()))

p = [Vector(1, 2), Vector(2, 4), Vector(3, 11)]

v = [] # v ==> Vandermonde matrix
y = []

for i in range(len(p)):
    temp = []
    for j in range(len(p)):
        temp.append(p[i].x ** j)
    v.append(temp)
    y.append([p[i].y])

# calculating the determinant of the Vandermonde matrix using a product
det_v = 1
for i in range(len(p)):
    for j in range(i, len(p)):
        if i < j:
            det_v *= p[j].x - p[i].x

print(det(v), det_v, det(v) == det_v)
coeffs = mMult(mInv(v), y)

print(coeffs)