import math

def extend(input_string):
    temp = int(math.ceil(math.log2(len(input_string) + 3))) # 2, 4, 6, 8, 10, ...
    m_size = int(math.sqrt(2 ** temp)) # 2, 4, 8, 16, 32, ...
    m_1 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] # m ==> matrix

    for i in range(1, 16):
        x = math.log2(i)
        if x != math.floor(x):
            row = i // 4
            m_1[row][i - 4 * row] = int(input_string[0])
            try:
                input_string = input_string[1:]
            except:
                pass

    for i in range(temp // 2): # 1, 2, 3, 4, 5, ..., for rows = cols = 8, i will be 0, 1, 2
        c = 0
        s_1 = 0
        s_2 = 0
        for j in range(int(m_size // (2 ** (i + 1)))): # for rows = cols = 8, j_max will be 4, 2, 1
            c += 2 ** i
            for k in range(2 ** i):
                for l in range(m_size):
                    if m_1[l][c]:
                        s_1 += 1
                    if m_1[c][l]:
                        s_2 += 1
                c += 1
        if s_1 % 2:
            pos_num = 2 ** i
            m_1[pos_num // m_size][pos_num % m_size] = 1
        if s_2 % 2:
            pos_num = 2 ** (i + temp // 2)
            m_1[pos_num // m_size][pos_num % m_size] = 1

    s = 0
    for i in m_1:
        for j in i:
            if j:
                s += 1
    if s % 2:
        m_1[0][0] = 1

    return m_1

def checkForErrors(m): # m ==> matrix
    temp = 2 * int(math.log2(len(m))) # 2, 4, 6, 8, 10, ...
    m_size = int(math.sqrt(2 ** temp)) # 2, 4, 8, 16, 32, ...
    m_errors = []

    for i in range(temp // 2): # 1, 2, 3, 4, 5, ..., for rows = cols = 8, i will be 0, 1, 2
        c = 0
        s_1 = 0
        s_2 = 0
        for j in range(int(m_size // (2 ** (i + 1)))): # for rows = cols = 8, j_max will be 4, 2, 1
            c += 2 ** i
            for k in range(2 ** i):
                for l in range(m_size):
                    if m[l][c]:
                        s_1 += 1
                    if m[c][l]:
                        s_2 += 1
                c += 1
        if s_1 % 2:
            m_errors.append(2 ** i)
        if s_2 % 2:
            m_errors.append(2 ** (i + temp // 2))

    s = 0
    for i in m:
        for j in i:
            if j:
                s += 1

    return [bool(s % 2), m_errors]

def correct(m, parity_error, m_errors):
    pos_num = 0
    n = len(m)
    for i in m_errors:
        pos_num += i
    if m_errors:
        if parity_error:
            if m[pos_num // n][pos_num % n]:
                m[pos_num // n][pos_num % n] = 0
            else:
                m[pos_num // n][pos_num % n] = 1
            return m
        else:
            return "Probably two errors."
    else:
        if parity_error:
            if m[0][0]:
                m[0][0] = 0
            else:
                m[0][0] = 1
            return m
        else:
            return "Probably no errors."

temp = extend("11101110000")
for i in temp:
    print(i)
r = 0
c = 2
if temp[r][c]:
    temp[r][c] = 0
else:
    temp[r][c] = 1
# r = 0
# c = 0
# if temp[r][c]:
#     temp[r][c] = 0
# else:
#     temp[r][c] = 1
print()
for i in temp:
    print(i)
print()
temp_2 = checkForErrors(temp)
temp_3 = correct(temp, temp_2[0], temp_2[1])
if type(temp_3) == str:
    print(temp_3)
else:
    for i in temp_3:
        print(i)