from PIL import Image

rating_int = 2 # 0 ==> s; 1 ==> q; 2 ==> e

fp = open(f"ai_dataset_2/category_{rating_int}/category_{rating_int}_count.txt", 'r')
curr_img_cnt = int(fp.readline())
fp.close()

fp = open(f"ai_dataset_2/category_{rating_int}_formatted/category_{rating_int}_formatted_count.txt", 'r')
curr_form_img_cnt = int(fp.readline())
fp.close()

for i in range(curr_form_img_cnt, curr_img_cnt):
    im = Image.open(f"ai_dataset_2/category_{rating_int}/category_{rating_int}_img_{i}.jpg")
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

    resized_img.save(f"ai_dataset_2/category_{rating_int}_formatted/category_{rating_int}_formatted_img_{i}.png")
    # resized_img.save(f"../ai_dataset_2/category_0_formatted/category_0_formatted_img_{i}.jpg")
    # resized_img.save(f"../ai_dataset_2/category_1_formatted/category_1_formatted_img_{i}.jpg")
    # resized_img.save(f"../ai_dataset_2/test_images_formatted/formatted_test_img_{i}.jpg")

    resized_img.close()

    print(f"Saved \033[31m{i + 1}\033[0m / {curr_img_cnt}.")

fp = open(f"ai_dataset_2/category_{rating_int}_formatted/category_{rating_int}_formatted_count.txt", 'w')
fp.write(str(curr_img_cnt))
fp.close()

print("End of program.")
