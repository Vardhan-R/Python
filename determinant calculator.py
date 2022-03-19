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

print(det([[1, 2, 7, 9], [12, 21, 11, -8], [8, 17, 2, -5], [0, -4, -7, -2]]))