from PIL import Image
from built_modules import import_vectors as vect
import numpy as np

test_img_no = 6

def newPos(pixels_arr: np.ndarray, pos: vect.Vector, prev_pos: None | vect.Vector = None) -> vect.Vector:
    refer = {0: (pos.x + 1, pos.y), # right
    1: (pos.x + 1, pos.y + 1), # bottom-right
    2: (pos.x, pos.y + 1), # bottom
    3: (pos.x - 1, pos.y + 1), # bottom-left
    4: (pos.x - 1, pos.y), # left
    5: (pos.x - 1, pos.y - 1), # top-left
    6: (pos.x, pos.y - 1), # top
    7: (pos.x + 1, pos.y - 1)} # top-right

    flattened_grid_lst = [pixels_arr[refer[x][1], refer[x][0]] for x in range(8)]

    s = 0
    c = 0
    while True:
        c += 1
        for m in range(s, 8):
            if not(flattened_grid_lst[m][0]): # 1st black found
                break

        for n in range(m, 8):
            if flattened_grid_lst[n][0]: # not black found
                break
        else:
            n = 0

        new_pos = vect.Vector(refer[n][0], refer[n][1])

        if new_pos != prev_pos or c > 2:
            break
        s = n

        # [w, w, w, w, w, w, b, b, b]; m = 6; n = 0
        # [w, w, w, w, b, b, b, w, w]; m = 4; n = 7

    return new_pos

im = Image.open(f"C:/Users/CSC/Desktop/CS/outlining_test_images/test_img_{test_img_no}.png", 'r')
img_size = im.size
pixels_lst = list(im.getdata())

pixels_arr = np.array(pixels_lst)
pixels_arr.resize(img_size[1], img_size[0], 3)

b = False
for i in range(img_size[1]): # row
    for j in range(img_size[0]): # col
        if pixels_arr[i][j][0]:
            pos = vect.Vector(j, i)
            path_lst = [(j, i)]

            b = True
            break
    if b:
        break

pos = newPos(pixels_arr, pos)
# while (pos.x, pos.y) != path_lst[0]:
for _ in range(2000):
    path_lst.append((pos.x, pos.y))
    pos = newPos(pixels_arr, pos, vect.Vector(path_lst[-2][0], path_lst[-2][1]))

txt_file = open(f"C:/Users/CSC/Desktop/CS/python_files/outlined_data_{test_img_no}.txt", 'w')
for i in path_lst:
    txt_file.write(f"{i[0]} {i[1]}\n")
txt_file.close()