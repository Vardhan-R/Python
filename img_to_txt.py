from PIL import Image

for i in range(20):
    im = Image.open(f"ai_dataset/test_images_formatted/test_img_{i}_category_{int(4 < i < 15)}.png")
    pixels_lst = list(im.getdata())
    img_size = im.size # width (x-axis), height (y-axis)

    txt_file = open(f"ai_dataset/test_images_formatted/all_test_images_formatted.txt", 'a')

    txt_file.write(f"{img_size[0]} {img_size[1]}\n")

    for j in range(img_size[1]):
        txt_file.write(" ".join([str(x) for x in pixels_lst[j]]) + '\n')

    txt_file.close()