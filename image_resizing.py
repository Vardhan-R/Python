from PIL import Image

rating = 0 # 0 ==> s; 1 ==> q; 2 ==> e

for i in range(40, 80):
    im = Image.open(f"../ai_dataset_2/category_{rating}/category_{rating}_img_{i}.jpg")
    # im = Image.open(f"../ai_dataset_2/category_0/category_0_img_{i}.jpg")
    # im = Image.open(f"../ai_dataset_2/category_1/category_1_img_{i}.jpg")
    # im = Image.open(f"../ai_dataset_2/test_images/test_img_{i}.jpg")
    resized_img = im.resize((128, 128))
    im.close()
    # pixels_lst = list(im.getdata())
    # img_size = im.size # width (x-axis), height (y-axis)

    # txt_file = open(f"C:/Users/vrdhn/Desktop/CS/test_file_1.txt", 'w')

    # txt_file.write(f"{img_size[0]} {img_size[1]}\n")

    # for j in range(img_size[0] * img_size[1]):
    #     print(j, img_size[0] * img_size[1])
    #     txt_file.write(";".join([str(x) for x in pixels_lst[j]]) + 'm\n')

    # txt_file.close()

    resized_img.save(f"../ai_dataset_2/category_{rating}_formatted/category_{rating}_formatted_img_{i}.jpg")
    # resized_img.save(f"../ai_dataset_2/category_0_formatted/category_0_formatted_img_{i}.jpg")
    # resized_img.save(f"../ai_dataset_2/category_1_formatted/category_1_formatted_img_{i}.jpg")
    # resized_img.save(f"../ai_dataset_2/test_images_formatted/formatted_test_img_{i}.jpg")

    resized_img.close()

    print(f"Saved {i + 1} / 80")

print("End of program")