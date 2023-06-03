from built_modules import import_vectors as vect
from PIL import Image
from matplotlib import patches, pyplot as plt
import numpy as np

def step(arr: np.ndarray, pos: tuple, direc: str) -> tuple[tuple[int, int], str]:
    if direc == 'd': # facing down
        if arr[pos[0]][pos[1] + 1][0]: # left
            return ((pos[0], pos[1] + 1), 'r')
        if arr[pos[0] + 1][pos[1]][0]: # forward
            return ((pos[0] + 1, pos[1]), 'd')
        if arr[pos[0]][pos[1] - 1][0]: # right
            return ((pos[0], pos[1] - 1), 'l')
        return ((pos[0] - 1, pos[1]), 'u') # backward
    if direc == 'r': # facing right
        if arr[pos[0] - 1][pos[1]][0]: # left
            return ((pos[0] - 1, pos[1]), 'u')
        if arr[pos[0]][pos[1] + 1][0]: # forward
            return ((pos[0], pos[1] + 1), 'r')
        if arr[pos[0] + 1][pos[1]][0]: # right
            return ((pos[0] + 1, pos[1]), 'd')
        return ((pos[0], pos[1] - 1), 'l') # backward
    if direc == 'u': # facing up
        if arr[pos[0]][pos[1] - 1][0]: # left
            return ((pos[0], pos[1] - 1), 'l')
        if arr[pos[0] - 1][pos[1]][0]: # forward
            return ((pos[0] - 1, pos[1]), 'u')
        if arr[pos[0]][pos[1] + 1][0]: # right
            return ((pos[0], pos[1] + 1), 'r')
        return ((pos[0] + 1, pos[1]), 'd') # backward
    # facing left
    if arr[pos[0] + 1][pos[1]][0]: # left
            return ((pos[0] + 1, pos[1]), 'd')
    if arr[pos[0]][pos[1] - 1][0]: # forward
        return ((pos[0], pos[1] - 1), 'l')
    if arr[pos[0] - 1][pos[1]][0]: # right
        return ((pos[0] - 1, pos[1]), 'u')
    return ((pos[0], pos[1] + 1), 'r') # backward

def xor(a, b):
    return a and not(b) or not(a) and b

im = Image.open("circuits/circuit_4.png")
px = np.array(im.getdata())
im.close()
temp = round(np.sqrt(px.size / px.shape[1]))
px = px.reshape((temp, temp, px.shape[1]))[:, :, :3]
dim = px.shape

path = []
direc = 'r'
f = True

for i in range(dim[0]):
    if f:
        for j in range(dim[1]):
            if px[i][j][0]:
                path.append((i, j))
                f = False
                break

nxt_step = (-1, -1)
while True:
    nxt_step, direc = step(px, path[-1], direc)
    if nxt_step == path[0]:
        break
    path.append(nxt_step)

# for i in range(len(path)):
#     # path[i] = path[i][0] + 1j * path[i][1]
#     path[i] = vect.Vector(path[i][1], path[i][0])

clr = np.zeros(dim)

# for i in range(dim[0]):
#     for j in range(dim[1]):
#         pt = vect.Vector(j, i)
#         a = 0
#         f = True
#         for k in range(len(path)):
#             try:
#             #     a += np.angle((path[i - 1] - pt) / (path[i] - pt))
#                 a += vect.angBetween(vect.sub(path[i], pt), vect.sub(path[i - 1], pt))
#             except:
#                 clr[i][j][0] = 1
#                 f = False
#                 break
#         if f:
#             # temp = int(a > np.pi)
#             # print(a)
#             clr[i][j][2] = int(a > np.pi)

# clr = [(int((i, j) in path), int((i, j) in path), int((i, j) in path)) for j in range(dim[1]) for i in range(dim[0])]

for i in range(dim[0]):
    inside = False
    prev_inside = False
    long_wall = False
    prev = False
    for j in range(dim[1]):
        curr = (i, j) in path
        if curr and not(prev):
            temp_top = (i - 1, j) in path
            temp_bot = (i + 1, j) in path
            v = int(temp_bot) - int(temp_top)
            long_wall = not(temp_top and temp_bot)
            prev_inside = inside
            inside = False
        elif not(curr) and prev:
            # if long_wall:
            #     if (v == -1 and (i + 1, j - 1) in path) or (v == 1 and (i - 1, j - 1) in path):
            #         inside = not(prev_inside)
            #     else:
            #         inside = prev_inside
            #     # inside = xor((v == -1 and (i + 1, j - 1) in path) or (v == 1 and (i - 1, j - 1) in path), prev_inside)
            #     long_wall = False
            # else:
            #     inside = not(prev_inside)
            # if (long_wall and (v == -1 and (i + 1, j - 1) in path) or (v == 1 and (i - 1, j - 1) in path)) or not(long_wall):
            #     inside = not(prev_inside)
            # long_wall = False
            # if long_wall:
            #     inside = xor(long_wall and (v == -1 and (i + 1, j - 1) in path) or (v == 1 and (i - 1, j - 1) in path), xor(prev_inside, long_wall))
            # else:
            #     inside = not(prev_inside)
            temp = (v == -1 and (i + 1, j - 1) in path) or (v == 1 and (i - 1, j - 1) in path)
            inside = temp and not(prev_inside or not(long_wall)) or not(temp) and xor(prev_inside, (not(long_wall)))
            long_wall = False
        prev = curr

        clr[i][j][0] = int(curr)
        clr[i][j][2] = int(inside)

    # for j in range(dim[1] - 1, -1, -1):
    #     curr = (i, j) in path
    #     if curr and not(prev):
    #         temp_top = (i - 1, j) in path
    #         temp_bot = (i + 1, j) in path
    #         v = int(temp_bot) - int(temp_top)
    #         long_wall = not(temp_top and temp_bot)
    #         prev_inside = inside
    #         inside = False
    #     if not(curr) and prev:
    #         # if long_wall:
    #         #     if (v == -1 and (i + 1, j - 1) in path) or (v == 1 and (i - 1, j - 1) in path):
    #         #         inside = not(inside)
    #         #     long_wall = False
    #         # else:
    #         #     inside = not(inside)
    #         if (long_wall and (v == -1 and (i + 1, j + 1) in path) or (v == 1 and (i - 1, j + 1) in path)) or not(long_wall):
    #             inside = not(inside)
    #         long_wall = False
    #     prev = curr

    #     if inside:
    #         clr[i][j][2] = int(inside)
    #         # clr[i, j:, 2] += int(curr and (not(prev)))
    #         # clr[i, :(j), 1] += int(curr and (not(prev)))

clr %= 2

plt.rcParams["figure.figsize"] = (7, 7)
ax = plt.figure().add_subplot()
for i in range(dim[0]):
    for j in range(dim[1]):
        # if clr[i][j][1] and clr[i][j][2]:
        #     ax.add_patch(patches.Rectangle((j, i), 1, 1, facecolor=(int((i, j) in path), clr[i][j][1], clr[i][j][2])))
        # else:
        #     ax.add_patch(patches.Rectangle((j, i), 1, 1, facecolor=(int((i, j) in path), 0, 0)))
        # ax.add_patch(patches.Rectangle((j, i), 1, 1, facecolor=clr[i][j]))
        # if (i, j) in path:
        #     ax.add_patch(patches.Rectangle((j, i), 1, 1, facecolor=(1, clr[i][j][1], clr[i][j][2])))
        ax.add_patch(patches.Rectangle((j, i), 1, 1, facecolor=clr[i][j]))
plt.xlim(0, dim[1])
plt.ylim(0, dim[0])
plt.show()



# p = path

# pts = []
# all_pts = []
# nN = len(p)
# freqs = []
# coeffs = []

# class Comp:
#     def __init__(self, r, i):
#         self.r = r
#         self.i = i
#         self.z = str(r) + " + " + str(i) + "i"

#     def copy(self): return Comp(self.r, self.i)

#     def mag(self): return np.sqrt(self.r ** 2 + self.i ** 2)

#     def magSq(self): return self.r ** 2 + self.i ** 2

#     def normalise(self): return self.write(self.r / self.mag(), self.i / self.mag())

#     def setMag(self, m):
#         try:
#             old_mag = self.mag()
#             self.r = m * self.r / old_mag
#             self.i = m * self.i / old_mag
#         except: pass

#     def angle(self):
#         if np.arctan2(self.i, self.r) < 0: return 2 * np.pi + np.arctan2(self.i, self.r)
#         else: return np.arctan2(self.i, self.r)

#     # def plot(self, clr):
#     #     pygame.draw.circle(scrn, clr, (width * (xl - self.r) / (xl - xr), height * (yu - self.i) / (yu - yd)), 4)

# def add(z1, z2): return Comp(z1.r + z2.r, z1.i + z2.i)
# def mult(z1, z2): return Comp(z1.r * z2.r - z1.i * z2.i, z1.r * z2.i + z1.i * z2.r)

# for i in p:
#     pts.append(Comp(i[0], i[1]))

# for i in range(round(-(nN - 1) / 2), round((nN + 1) / 2)):
#     freqs.append(i)

# for i in freqs:
#     c = Comp(0, 0)
#     for j in range(nN):
#         c = add(c, mult(pts[j], Comp(np.cos(2 * np.pi * i * j / nN), -np.sin(2 * np.pi * i * j / nN))))
#     coeffs.append(c)

# for i in range(nN):
#     coeffs[i] = coeffs[i][0] + 1j * coeffs[i][1]

# def func(x):
#     y = 0
#     for i in range(nN):
#         y += np.exp(2 * np.pi * freqs)