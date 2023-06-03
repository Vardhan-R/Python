from PIL import Image

rating_int = 0

for i in range(1):
    im = Image.open(f"tst_img_1.png")
    pixels_lst = list(im.getdata())
    im.close()
    img_size = im.size # width (x-axis), height (y-axis)

    pixel_cnt = img_size[0] * img_size[1]

    str_to_write = f"{img_size[0]} {img_size[1]}\n"

    for j in range(pixel_cnt):
        # txt_file.write(";".join([str(x) for x in pixels_lst[j]]) + 'm\n')

        str_to_write += " ".join([str(x) for x in pixels_lst[j][:3]]) + "\n"
        print(f"{j + 1} / {pixel_cnt}")
    txt_file = open(f"test_file_1.txt", 'w')
    txt_file.write(str_to_write)
    txt_file.close()
