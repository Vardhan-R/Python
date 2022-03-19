def formatting(s):
    l = []
    t = ""
    for m in range(len(s)):
        if m % 2: l.append(s[m].lower())
        else: l.append(s[m].upper())
    for m in l: t += m
    print(t)
formatting("vaccines insert microchips into our bodies which let the fbi track our every move and 5g causes cancer")