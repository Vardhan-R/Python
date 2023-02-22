from PIL import Image
import matplotlib.pyplot as plt, numpy as np

txt_file = open("../ai_dataset/all_txt_files/category_0_all_images.txt", 'r')

for i in range(3):
    temp_lst = txt_file.readline()[:-1].split(" ") # ["width", "height"]
    img_size = tuple([int(x) for x in temp_lst]) # (width, height)
    pixels_lst = []
    for j in range(img_size[1]):
        temp_lst_1 = []
        for k in range(img_size[0]):
            temp_lst_2 = txt_file.readline()[:-1].split(" ") # ["r_value", "g_value", "b_value"]
            pixel_tpl = tuple([int(x) for x in temp_lst_2]) # (r_value, g_value, b_value)
            temp_lst_1.append(pixel_tpl)
        pixels_lst.append(temp_lst_1.copy())

    img = Image.new("RGB", img_size)

    pix = img.load()

    for j in range(img_size[1]): # row number (y-axis)
        for k in range(img_size[0]): # col number (x-axis)
            pix[k, j] = pixels_lst[j][k]

    img.save(f"../ai_dataset/category_0/category_0_img_{i}.jpg")

    print(f"{i + 1} / 102")

txt_file.close()