from PIL import Image
import numpy as np, random

test_img_no = 6
im = Image.open(f"C:/Users/CSC/Desktop/CS/outlining_test_images/test_img_{test_img_no}.jpg", 'r')

pixels_arr = np.array(list(im.getdata()))
img_size = im.size # width (cols) (x-axis), height (rows) (y-axis)
pixels_arr.resize((img_size[1], img_size[0], 3))

diff_arr = np.full((img_size[1], img_size[0]), 0)

for i in range(img_size[1] - 1): # row
    for j in range(img_size[0] - 1): # col
        # not checking last row and col
        # only checking the right and the below pixels for each pixel
        for k in range(3):
            diff_arr[i][j] += abs(pixels_arr[i][j][k] - pixels_arr[i][j + 1][k]) + abs(pixels_arr[i][j][k] - pixels_arr[i + 1][j][k]) # right + below

# temp = diff_arr.reshape(-1)
# temp[::-1].sort()
# print(temp[:10])

threshold = 200

pix = im.load()

for i in range(img_size[1]): # row
    for j in range(img_size[0]): # col
        # white
        temp = 255 * int(diff_arr[i][j] >= threshold)
        pix[j, i] = (temp, temp, temp)

        # if diff_arr[i][j] < threshold:
        #     pix[j, i] = (0, 0, 0)
        # else:
            # random
            # pix[j, i] = (random.randrange(256), random.randrange(256), random.randrange(256))

            # red to blue (left to right)
            # pix[j, i] = (round(255 * (1 - j / img_size[0])), 0, round(255 * j / img_size[0]))

            # red to blue (top to bottom)
            # pix[j, i] = (round(255 * (1 - i / img_size[1])), 0, round(255 * i / img_size[1]))

            # red to blue (diagonally)
            # pix[j, i] = (round(255 * (1 - (i + j) / (img_size[0] + img_size[1]))), 0, round(255 * (i + j) / (img_size[0] + img_size[1])))

            # red to blue (other diagonal)
            # pix[j, i] = (round(255 * (1 - (i - j + img_size[1]) / (img_size[0] + img_size[1]))), 0, round(255 * (i - j + img_size[1]) / (img_size[0] + img_size[1])))

            # green to yellow (left to right)
            # pix[j, i] = (round(255 * j / img_size[0]), 255, 0)

im.save("enhanced_img.png")
