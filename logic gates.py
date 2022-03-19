a = 0
b = 0
c = 0
d = 0
def nott(x):
    return(int(not(x)))

def andd(x, y):
    return(int(x and y))

def orr(x, y):
    return(int(x or y))

def xor(x, y):
    if x == y:
        return 0
    else:
        return 1

for i in range(16):
    if a == 2:
        a = 0
        b += 1
    if b == 2:
        b = 0
        c += 1
    if c == 2:
        c = 0
        d += 1
    # print(d, c, b, a, ":", orr((andd(b, xor(d, b))), andd(andd(xor(c, a), a), nott(xor(d, b)))), "and")
    print(d, c, b, a, ":", andd(andd(a, xor(c, a)), xor(andd(a, xor(c, a)), d)), xor(b, andd(d, andd(a, xor(c, a)))), xor(c, a))
    a += 1

# xor(c, a)
# xor(b, andd(d, andd(a, xor(c, a))))
# andd(andd(a, xor(c, a)), xor(andd(a, xor(c, a)), d))