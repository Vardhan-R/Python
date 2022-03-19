def convertNum(num, from_base, to_base, min_op_str_len = None): # min_op_str_len ==> minimum output string length
    num = str(num)
    l = []
    r = 0
    for i in num:
        if i == "A":
            l.append(10)
        elif i == "B":
            l.append(11)
        elif i == "C":
            l.append(12)
        elif i == "D":
            l.append(13)
        elif i == "E":
            l.append(14)
        elif i == "F":
            l.append(15)
        elif i == "G":
            l.append(16)
        elif i == "H":
            l.append(17)
        elif i == "I":
            l.append(18)
        elif i == "J":
            l.append(19)
        elif i == "K":
            l.append(20)
        elif i == "L":
            l.append(21)
        elif i == "M":
            l.append(22)
        elif i == "N":
            l.append(23)
        elif i == "O":
            l.append(24)
        elif i == "P":
            l.append(25)
        elif i == "Q":
            l.append(26)
        elif i == "R":
            l.append(27)
        elif i == "S":
            l.append(28)
        elif i == "T":
            l.append(29)
        elif i == "U":
            l.append(30)
        elif i == "V":
            l.append(31)
        elif i == "W":
            l.append(32)
        elif i == "X":
            l.append(33)
        elif i == "Y":
            l.append(34)
        elif i == "Z":
            l.append(35)
        else:
            l.append(i)
    l.reverse()
    f = 0
    for i in range(len(num)):
        f = f + int(l[i]) * from_base ** i
    l.clear()
    while f != 0:
        r = f % to_base
        f = f // to_base
        l.append(r)
    l.reverse()
    for i in range(len(l)):
        if l[i] == 10:
            l[i] = "A"
        elif l[i] == 11:
            l[i] = "B"
        elif l[i] == 12:
            l[i] = "C"
        elif l[i] == 13:
            l[i] = "D"
        elif l[i] == 14:
            l[i] = "E"
        elif l[i] == 15:
            l[i] = "F"
        elif l[i] == 16:
            l[i] = "G"
        elif l[i] == 17:
            l[i] = "H"
        elif l[i] == 18:
            l[i] = "I"
        elif l[i] == 19:
            l[i] = "J"
        elif l[i] == 20:
            l[i] = "K"
        elif l[i] == 21:
            l[i] = "L"
        elif l[i] == 22:
            l[i] = "M"
        elif l[i] == 23:
            l[i] = "N"
        elif l[i] == 24:
            l[i] = "O"
        elif l[i] == 25:
            l[i] = "P"
        elif l[i] == 26:
            l[i] = "Q"
        elif l[i] == 27:
            l[i] = "R"
        elif l[i] == 28:
            l[i] = "S"
        elif l[i] == 29:
            l[i] = "T"
        elif l[i] == 30:
            l[i] = "U"
        elif l[i] == 31:
            l[i] = "V"
        elif l[i] == 32:
            l[i] = "W"
        elif l[i] == 33:
            l[i] = "X"
        elif l[i] == 34:
            l[i] = "Y"
        elif l[i] == 35:
            l[i] = "Z"
    f = ""
    for i in l:
        f += str(i)
    if min_op_str_len:
        while len(f) < min_op_str_len:
            f = "0" + f
    return f