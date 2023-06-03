from PIL import Image
import numpy as np

cat_0_img_cnt = 1000
s = ""

for i in range(cat_0_img_cnt):
    im = Image.open(f"ai_dataset_3/category_0_formatted/category_0_formatted_img_{i}.png", 'r')
    pixels_arr = np.array(list(im.getdata()), dtype=str)
    im.close()
    pixels_arr = pixels_arr.flatten()
    s += "\n".join(pixels_arr) + "\n"

    print(f"Opened image \033[31m{i}\033[0m. {cat_0_img_cnt} total images.")

fp = open("cat_0_pure_2.txt", 'w')
fp.write(s)
fp.close()