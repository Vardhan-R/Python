import math, time

full_lst = []
spots = []

for i in range(3):
    for j in range(3):
        spots.append((i, j))

for i_1 in spots:
    for i_2 in spots:
        if i_2 not in [i_1]:
            print(i_1, i_2)
            for i_3 in spots:
                if i_3 not in [i_1, i_2]:
                    for i_4 in spots:
                        if i_4 not in [i_1, i_2, i_3]:
                            for i_5 in spots:
                                if i_5 not in [i_1, i_2, i_3, i_4]:
                                    for i_6 in spots:
                                        if i_6 not in [i_1, i_2, i_3, i_4, i_5]:
                                            for i_7 in spots:
                                                if i_7 not in [i_1, i_2, i_3, i_4, i_5, i_6]:
                                                    for i_8 in spots:
                                                        if i_8 not in [i_1, i_2, i_3, i_4, i_5, i_6, i_7]:
                                                            for i_9 in spots:
                                                                if i_9 not in [i_1, i_2, i_3, i_4, i_5, i_6, i_7, i_8]:
                                                                    full_lst.append([i_1, i_2, i_3, i_4, i_5, i_6, i_7, i_8, i_9])

print(len(full_lst), math.factorial(9))
time.sleep(5)

# spots = [(0, 0), (0, 1), (1, 0), (1, 1)]

# for i_1 in spots:
#     for i_2 in spots:
#         for i_3 in spots:
#             for i_4 in spots:
#                 lst = []
#                 lst.append(i_1)
#                 if i_2 not in lst:
#                     lst.append(i_2)
#                 if i_3 not in lst:
#                     lst.append(i_3)
#                 if i_4 not in lst:
#                     lst.append(i_4)
#                 if len(lst) == 4:
#                     full_lst.append(lst.copy())
# print(full_lst)

for i in full_lst:
    print(i[0], i[1], i[2])
    c = 0
    for j in range(len(i) - 1): # 0 to 7
        if i[j] != (1, 1):
            for k in range(j, len(i)): # j to 8
                if i[j] == (0, 0) and i[k] == (0, 2) and (0, 1) not in i[:k]: # tl
                    full_lst.remove(i)
                    c = 1
                    break
                elif i[j] == (0, 0) and i[k] == (2, 0) and (1, 0) not in i[:k]: # tl
                    full_lst.remove(i)
                    c = 1
                    break
                elif i[j] == (0, 0) and i[k] == (2, 2) and (1, 1) not in i[:k]: # tl
                    full_lst.remove(i)
                    c = 1
                    break
                elif i[j] == (0, 1) and i[k] == (2, 1) and (1, 1) not in i[:k]: # t
                    full_lst.remove(i)
                    c = 1
                    break
                elif i[j] == (0, 2) and i[k] == (0, 0) and (0, 1) not in i[:k]: # tr
                    full_lst.remove(i)
                    c = 1
                    break
                elif i[j] == (0, 2) and i[k] == (2, 0) and (1, 1) not in i[:k]: # tr
                    full_lst.remove(i)
                    c = 1
                    break
                elif i[j] == (0, 2) and i[k] == (2, 2) and (1, 2) not in i[:k]: # tr
                    full_lst.remove(i)
                    c = 1
                    break
                elif i[j] == (1, 0) and i[k] == (1, 2) and (1, 1) not in i[:k]: # l
                    full_lst.remove(i)
                    c = 1
                    break
                elif i[j] == (1, 2) and i[k] == (1, 0) and (1, 1) not in i[:k]: # r
                    full_lst.remove(i)
                    c = 1
                    break
                elif i[j] == (2, 0) and i[k] == (0, 0) and (1, 0) not in i[:k]: # bl
                    full_lst.remove(i)
                    c = 1
                    break
                elif i[j] == (2, 0) and i[k] == (0, 2) and (1, 1) not in i[:k]: # bl
                    full_lst.remove(i)
                    c = 1
                    break
                elif i[j] == (2, 0) and i[k] == (2, 2) and (2, 1) not in i[:k]: # bl
                    full_lst.remove(i)
                    c = 1
                    break
                elif i[j] == (2, 1) and i[k] == (0, 1) and (1, 1) not in i[:k]: # b
                    full_lst.remove(i)
                    c = 1
                    break
                elif i[j] == (2, 2) and i[k] == (0, 0) and (1, 1) not in i[:k]: # br
                    full_lst.remove(i)
                    c = 1
                    break
                elif i[j] == (2, 2) and i[k] == (0, 2) and (1, 2) not in i[:k]: # br
                    full_lst.remove(i)
                    c = 1
                    break
                elif i[j] == (2, 2) and i[k] == (2, 0) and (2, 1) not in i[:k]: # br
                    full_lst.remove(i)
                    c = 1
                    break
            if c:
                break

print(len(full_lst))