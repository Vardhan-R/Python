from PIL import Image

for i in range(1):
    im = Image.open(f"C:/Users/vrdhn/Desktop/CS/ai_dataset_2/category_0/category_0_img_2.jpg")
    pixels_lst = list(im.getdata())
    img_size = im.size # width (x-axis), height (y-axis)

    txt_file = open(f"C:/Users/vrdhn/Desktop/CS/test_file_1.txt", 'w')

    txt_file.write(f"{img_size[0]} {img_size[1]}\n")

    for j in range(img_size[0] * img_size[1]):
        print(j, img_size[0] * img_size[1])
        txt_file.write(";".join([str(x) for x in pixels_lst[j]]) + 'm\n')

    txt_file.close()
