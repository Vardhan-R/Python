from PIL import Image
import random

im = Image.open("apple.jpeg", 'r')

pixels_lst = list(im.getdata())
random.seed(10)
random.shuffle(pixels_lst)
img_size = im.size # width (x-axis), height (y-axis)
pix = im.load()

for i in range(img_size[1]):
    for j in range(img_size[0]):
        pix[j, i] = pixels_lst[img_size[0] * i + j]

im.save("edited_img.png")

im_2 = Image.open("edited_img.png", 'r')

pixels_lst = list(im_2.getdata())
img_size = im_2.size
pix = im_2.load()

lst = [x for x in range(img_size[0] * img_size[1])]
random.seed(10)
random.shuffle(lst)

for i in range(img_size[1]):
    for j in range(img_size[0]):
        temp_1 = img_size[0] * i + j
        temp_2 = lst[temp_1]
        pix[temp_2 % img_size[0], temp_2 // img_size[0]] = pixels_lst[temp_1]

im_2.save("restored_img.png")
