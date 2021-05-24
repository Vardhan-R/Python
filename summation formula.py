import math
p = int(input("Power: "))
n = int(input("Number of Terms: "))
a = []
num = 0
den = 0
def comb(x, y):
    return(math.factorial(x) / (math.factorial(y) * math.factorial(x - y)))
for r in range(p + 2):
    numSub = 0
    for m in range(1, r + 2):
        numSub += m ** p
    num += (-1) ** (p - r + 1) * comb(p + 1, r) * numSub
for r in range(1, p + 3):
    den += (-1) ** (p - r + 2) * comb(p + 1, r - 1) * r ** (p + 1)
a.append(num / den)

for i in range(p, -1, -1):
    numSub1 = 0
    for r in range(i + 1):
        numSub11 = 0
        for m in range(1, r + 2):
            numSub11 += m ** p
        numSub1 += (-1) ** (i - r) * comb(i, r) * numSub11
    numSub2 = 0
    for j in range(i + 1, p + 2):
        numSub22 = 0
        for r in range(1, i + 2):
            numSub22 += (-1) ** (i + 1 - r) * comb(i, r - 1) * r ** j
        numSub2 += a[p + 1 - j] * numSub22
    den = 0
    for r in range (1, i + 2):
        den += (-1) ** (i + 1 - r) * comb(i, r - 1) * r ** i
    a.append((numSub1 - numSub2) / den)
form = ""
ans = 0
for i in range(len(a)):
    form += str(a[i]) + "n ^ " + str(len(a) - i - 1) + " + "
    ans += a[i] * n ** (len(a) - i - 1)
print(form[:-8])
print(round(ans))