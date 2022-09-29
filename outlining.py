from PIL import Image
from built_modules import import_vectors as vect
import math, numpy as np

def newPos(arr: np.ndarray, pos: vect.Vector, size: int, d: str):
    half_size = int((size - 1) / 2)
    grid = arr[(pos.y - half_size): (pos.y + half_size + 1), (pos.x - half_size): (pos.x + half_size + 1)]

    # if d == "right":
    #     if grid[half_size][-1][0]: # middle-right
    #         return vect.Vector(pos.x + 1, pos.y), "right"

    #     for i in grid[(half_size + 1):, -1]: # right column bottom half
    #         if i[0]:
    #             return vect.Vector(pos.x + 1, pos.y + 1), "right"

    #     for i in grid[-1, (half_size + 1):]: # bottom row right half
    #         if i[0]:
    #             return vect.Vector(pos.x + 1, pos.y + 1), "down"

    #     if grid[-1][half_size][0]: # bottom-middle
    #         return vect.Vector(pos.x, pos.y + 1), "down"

    #     for i in grid[-1, :half_size]: # bottom row left half
    #         if i[0]:
    #             return vect.Vector(pos.x - 1, pos.y + 1), "down"

    #     for i in grid[(half_size + 1):, 0]: # left column bottom half
    #         if i[0]:
    #             return vect.Vector(pos.x - 1, pos.y + 1), "left"

    #     if grid[half_size][0][0]: # middle-left
    #         return vect.Vector(pos.x - 1, pos.y), "left"

    #     for i in grid[:half_size, 0]: # left column top half
    #         if i[0]:
    #             return vect.Vector(pos.x - 1, pos.y - 1), "left"

    #     for i in grid[0, :half_size]: # top row left half
    #         if i[0]:
    #             return vect.Vector(pos.x - 1, pos.y - 1), "up"

    #     if grid[0][half_size][0]: # top-middle
    #         return vect.Vector(pos.x, pos.y - 1), "up"

    #     for i in grid[0, (half_size + 1):]: # top row right half
    #         if i[0]:
    #             return vect.Vector(pos.x + 1, pos.y - 1), "up"

    #     for i in grid[:half_size, -1]: # right column top half
    #         if i[0]:
    #             return vect.Vector(pos.x + 1, pos.y - 1), "right"

    # elif d == "down":
    #     if grid[-1][half_size][0]: # bottom-middle
    #         return vect.Vector(pos.x, pos.y + 1), "down"

    #     for i in grid[-1, :half_size]: # bottom row left half
    #         if i[0]:
    #             return vect.Vector(pos.x - 1, pos.y + 1), "down"

    #     for i in grid[(half_size + 1):, 0]: # left column bottom half
    #         if i[0]:
    #             return vect.Vector(pos.x - 1, pos.y + 1), "left"

    #     if grid[half_size][0][0]: # middle-left
    #         return vect.Vector(pos.x - 1, pos.y), "left"

    #     for i in grid[:half_size, 0]: # left column top half
    #         if i[0]:
    #             return vect.Vector(pos.x - 1, pos.y - 1), "left"

    #     for i in grid[0, :half_size]: # top row left half
    #         if i[0]:
    #             return vect.Vector(pos.x - 1, pos.y - 1), "up"

    #     if grid[0][half_size][0]: # top-middle
    #         return vect.Vector(pos.x, pos.y - 1), "up"

    #     for i in grid[0, (half_size + 1):]: # top row right half
    #         if i[0]:
    #             return vect.Vector(pos.x + 1, pos.y - 1), "up"

    #     for i in grid[:half_size, -1]: # right column top half
    #         if i[0]:
    #             return vect.Vector(pos.x + 1, pos.y - 1), "right"

    #     if grid[half_size][-1][0]: # middle-right
    #         return vect.Vector(pos.x + 1, pos.y), "right"

    #     for i in grid[(half_size + 1):, -1]: # right column bottom half
    #         if i[0]:
    #             return vect.Vector(pos.x + 1, pos.y + 1), "right"

    #     for i in grid[-1, (half_size + 1):]: # bottom row right half
    #         if i[0]:
    #             return vect.Vector(pos.x + 1, pos.y + 1), "down"

    # elif d == "left":
    #     if grid[half_size][0][0]: # middle-left
    #         return vect.Vector(pos.x - 1, pos.y), "left"

    #     for i in grid[:half_size, 0]: # left column top half
    #         if i[0]:
    #             return vect.Vector(pos.x - 1, pos.y - 1), "left"

    #     for i in grid[0, :half_size]: # top row left half
    #         if i[0]:
    #             return vect.Vector(pos.x - 1, pos.y - 1), "up"

    #     if grid[0][half_size][0]: # top-middle
    #         return vect.Vector(pos.x, pos.y - 1), "up"

    #     for i in grid[0, (half_size + 1):]: # top row right half
    #         if i[0]:
    #             return vect.Vector(pos.x + 1, pos.y - 1), "up"

    #     for i in grid[:half_size, -1]: # right column top half
    #         if i[0]:
    #             return vect.Vector(pos.x + 1, pos.y - 1), "right"

    #     if grid[half_size][-1][0]: # middle-right
    #         return vect.Vector(pos.x + 1, pos.y), "right"

    #     for i in grid[(half_size + 1):, -1]: # right column bottom half
    #         if i[0]:
    #             return vect.Vector(pos.x + 1, pos.y + 1), "right"

    #     for i in grid[-1, (half_size + 1):]: # bottom row right half
    #         if i[0]:
    #             return vect.Vector(pos.x + 1, pos.y + 1), "down"

    #     if grid[-1][half_size][0]: # bottom-middle
    #         return vect.Vector(pos.x, pos.y + 1), "down"

    #     for i in grid[-1, :half_size]: # bottom row left half
    #         if i[0]:
    #             return vect.Vector(pos.x - 1, pos.y + 1), "down"

    #     for i in grid[(half_size + 1):, 0]: # left column bottom half
    #         if i[0]:
    #             return vect.Vector(pos.x - 1, pos.y + 1), "left"

    # else: # d == "up"
    #     if grid[0][half_size][0]: # top-middle
    #         return vect.Vector(pos.x, pos.y - 1), "up"

    #     for i in grid[0, (half_size + 1):]: # top row right half
    #         if i[0]:
    #             return vect.Vector(pos.x + 1, pos.y - 1), "up"

    #     for i in grid[:half_size, -1]: # right column top half
    #         if i[0]:
    #             return vect.Vector(pos.x + 1, pos.y - 1), "right"

    #     if grid[half_size][-1][0]: # middle-right
    #         return vect.Vector(pos.x + 1, pos.y), "right"

    #     for i in grid[(half_size + 1):, -1]: # right column bottom half
    #         if i[0]:
    #             return vect.Vector(pos.x + 1, pos.y + 1), "right"

    #     for i in grid[-1, (half_size + 1):]: # bottom row right half
    #         if i[0]:
    #             return vect.Vector(pos.x + 1, pos.y + 1), "down"

    #     if grid[-1][half_size][0]: # bottom-middle
    #         return vect.Vector(pos.x, pos.y + 1), "down"

    #     for i in grid[-1, :half_size]: # bottom row left half
    #         if i[0]:
    #             return vect.Vector(pos.x - 1, pos.y + 1), "down"

    #     for i in grid[(half_size + 1):, 0]: # left column bottom half
    #         if i[0]:
    #             return vect.Vector(pos.x - 1, pos.y + 1), "left"

    #     if grid[half_size][0][0]: # middle-left
    #         return vect.Vector(pos.x - 1, pos.y), "left"

    #     for i in grid[:half_size, 0]: # left column top half
    #         if i[0]:
    #             return vect.Vector(pos.x - 1, pos.y - 1), "left"

    #     for i in grid[0, :half_size]: # top row left half
    #         if i[0]:
    #             return vect.Vector(pos.x - 1, pos.y - 1), "up"

    if grid[half_size][-1][0]: # middle-right
        return vect.Vector(pos.x + 1, pos.y)

    for i in grid[(half_size + 1):, -1]: # right column bottom half
        if i[0]:
            return vect.Vector(pos.x + 1, pos.y + 1)

    for i in grid[:half_size, -1]: # right column top half
        if i[0]:
            return vect.Vector(pos.x + 1, pos.y - 1)

    for i in grid[-1, (half_size + 1):]: # bottom row right half
        if i[0]:
            return vect.Vector(pos.x + 1, pos.y + 1)

    for i in grid[0, (half_size + 1):]: # top row right half
        if i[0]:
            return vect.Vector(pos.x + 1, pos.y - 1)

    if grid[-1][half_size][0]: # bottom-middle
        return vect.Vector(pos.x, pos.y + 1)

    for i in grid[0, :half_size]: # top row left half
        if i[0]:
            return vect.Vector(pos.x - 1, pos.y - 1)

    for i in grid[-1, :half_size]: # bottom row left half
        if i[0]:
            return vect.Vector(pos.x - 1, pos.y + 1)

    if grid[0][half_size][0]: # top-middle
        return vect.Vector(pos.x, pos.y - 1)

    for i in grid[(half_size + 1):, 0]: # left column bottom half
        if i[0]:
            return vect.Vector(pos.x - 1, pos.y + 1)

    for i in grid[:half_size, 0]: # left column top half
        if i[0]:
            return vect.Vector(pos.x - 1, pos.y - 1)

    if grid[half_size][0][0]: # middle-left
        return vect.Vector(pos.x - 1, pos.y)

def newPosVect(arr: np.ndarray, path_pos: vect.Vector, path_prime_pos: vect.Vector, d: vect.Vector):
    path_pos = vect.add(path_pos, d)
    path_prime_pos = vect.add(path_prime_pos, d)

    path_clr = arr[path_pos.y][path_pos.x][0]
    path_prime_clr = arr[path_prime_pos.y][path_prime_pos.x][0]

    while not(path_clr and not(path_prime_clr)): # white and black
        if path_clr: # white
            path_pos = path_prime_pos
            path_prime_pos = vect.sub(path_prime_pos, d)
            d = d.rotate(-math.pi / 2)
            d.x = round(d.x)
            d.y = round(d.y)
        else: # path_clr is black
            if path_prime_clr: # white
                temp_vect = d.rotate(-math.pi / 2)
                temp_vect.x = round(temp_vect.x)
                temp_vect.y = round(temp_vect.y)
                path_pos = vect.add(path_pos, temp_vect)
                path_prime_pos = vect.add(path_prime_pos, temp_vect)
            else: # path_prime_clr is black
                temp_vect = d.rotate(math.pi / 2)
                temp_vect.x = round(temp_vect.x)
                temp_vect.y = round(temp_vect.y)
                path_pos = vect.add(path_pos, temp_vect)
                path_prime_pos = vect.add(path_prime_pos, temp_vect)
                path_prime_pos = path_pos
                path_pos = vect.sub(path_pos, d)
                d = temp_vect

        path_clr = arr[path_pos.y][path_pos.x][0]
        path_prime_clr = arr[path_prime_pos.y][path_prime_pos.x][0]

    return path_pos, path_prime_pos, d

    # if path_clr: # white
    #     if not(path_prime_clr): # black
    #         return path_pos, path_prime_pos, d
    #     else: # white
    #         d = d.rotate(-math.pi / 2)
    #         d.x = round(d.x)
    #         d.y = round(d.y)
    #         return path_prime_pos, vect.sub(path_prime_pos, d), d
    # else: # black
    #     if not(path_prime_clr): # black
    #         pass

im = Image.open("C:/Users/CSC/Desktop/test_img_2.png", 'r')
img_size = im.size
pixels_lst = list(im.getdata())

pixels_arr = np.array(pixels_lst)
pixels_arr.resize(img_size[1], img_size[0], 3)
# print(pixels_arr[0][0])

b = False
for i in range(img_size[1]): # row
    for j in range(img_size[0]): # col
        # if pixels_lst[i * img_size[0] + j][0]:
        if pixels_arr[i][j][0]:
            # k = i + 1
            # while pixels_lst[k * img_size[0] + j][0]:
            #     k += 1

            # r = (k - i) / 2

            path_pos = vect.Vector(j, i)
            path_prime_pos = vect.Vector(j, i - 1)
            d = vect.Vector(1, 0)
            # d = "right"

            b = True
            break
    if b:
        break

path_lst = [(path_pos.x, path_pos.y)]

for i in range(2699):
    # if d == "right":
    #     if pixels_arr[pos.y][pos.x + 1][0]: # check right
    #         pos.x += 1
    #     elif pixels_arr[pos.y + 1][pos.x][0]: # check bottom
    #         pos.y += 1
    #         d = "down"
    #     else: # check top
    #         pos.y -= 1
    #         d = "up"
    # elif d == "down":
    #     if pixels_arr[pos.y + 1][pos.x][0]: # check bottom
    #         pos.y += 1
    #     elif pixels_arr[pos.y][pos.x - 1][0]: # check left
    #         pos.x -= 1
    #         d = "left"
    #     else: # check right
    #         pos.x += 1
    #         d = "right"
    # elif d == "left":
    #     if pixels_arr[pos.y][pos.x - 1][0]: # check left
    #         pos.x -= 1
    #     elif pixels_arr[pos.y - 1][pos.x][0]: # check top
    #         pos.y -= 1
    #         d = "up"
    #     else: # check bottom
    #         pos.y += 1
    #         d = "down"
    # else: # d == "up"
    #     if pixels_arr[pos.y - 1][pos.x][0]: # check top
    #         pos.y -= 1
    #     elif pixels_arr[pos.y][pos.x + 1][0]: # check right
    #         pos.x += 1
    #         d = "right"
    #     else: # check left
    #         pos.x -= 1
    #         d = "left"

    # if pixels_arr[pos.y][pos.x + 1][0] and ((pos.x + 1, pos.y) not in path_lst): # check right
    #     pos.x += 1
    # elif pixels_arr[pos.y + 1][pos.x][0] and ((pos.x, pos.y + 1) not in path_lst): # check bottom
    #     pos.y += 1
    # elif pixels_arr[pos.y - 1][pos.x][0] and ((pos.x, pos.y - 1) not in path_lst): # check top
    #     pos.y -= 1
    # else: # check left
    #     pos.x -= 1

    # pos = newPos(pixels_arr, pos, 9, d)

    path_pos, path_prime_pos, d = newPosVect(pixels_arr, path_pos, path_prime_pos, d)

    path_lst.append((path_pos.x, path_pos.y))

# txt_file = open("C:/Users/CSC/Desktop/CS/python_files/outlined_data_2.txt", 'w')
# for i in path_lst:
#     txt_file.write(f"{i[0]} {i[1]}\n")
# txt_file.close()

# print(path_lst)