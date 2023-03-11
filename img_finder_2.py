from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image
import numpy as np, requests, time

# def intToStr(n: int):
#     return chr(-5 * n ** 2 + 3 * n + 115)

rating_int = 1 # 0 ==> s; 1 ==> q; 2 ==> e
rating_str = chr(-5 * rating_int ** 2 + 3 * rating_int + 115)

PATH = "D:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

fp = open(f"ai_dataset_2/category_{rating_int}/category_{rating_int}_count.txt", 'r')
curr_img_cnt = int(fp.readline())
fp.close()

fp = open(f"ai_dataset_2/category_{rating_int}/category_{rating_int}_edge_image_link.txt", 'r')
edge_img_link = fp.readline()
fp.close()

try:
    # for pg in range(8, 9):
    #     driver.get(f"https://yande.re/post?page={pg}&tags=rating%3A{rating_str}")
    #     # driver.get(f"https://yande.re/post?page={pg}&tags=rating%3As")
    #     # driver.get(f"https://yande.re/post?page={pg}&tags=rating%3Ae")
    #     # driver.get(f"https://yande.re/post?page={pg}&tags=rating%3Aq")
    #     # num_of_imgs = len(WebDriverWait(driver, 30).until(
    #     #     EC.presence_of_all_elements_located((By.CLASS_NAME, "plid"))
    #     # ))

    #     # for i in range(num_of_imgs):
    #     for i in range(14, 25):
    #         img_link = driver.find_element(By.XPATH, f'/html/body/div[8]/div[1]/div[2]/div[4]/ul/li[{i + 1}]/a').get_attribute("href")

    #         # img = Image.open(requests.get(img_link, stream = True, allow_redirects = True).raw)
    #         # img.save(f"../ai_dataset_2/category_0/category_0_img_{i}.jpg")

    #         response = requests.get(img_link)
    #         if response.status_code:
    #             fp = open(f"ai_dataset_2/category_{rating_int}/category_{rating_int}_img_{curr_img_cnt}.jpg", 'wb')
    #             # fp = open(f"../ai_dataset_2/category_0/category_0_img_{40 * (pg - 1) + i}.jpg", 'wb')
    #             # fp = open(f"../ai_dataset_2/category_1/category_1_img_{40 * (pg - 1) + i}.jpg", 'wb')
    #             # fp = open(f"../ai_dataset_2/test_images/test_img_{40 * (pg - 1) + i}.jpg", 'wb')
    #             fp.write(response.content)
    #             fp.close()

    #             curr_img_cnt += 1

    #         # print(f"Saved {i + 1} / {num_of_imgs}")
    #         print(f"Image \033[31m{i + 1}\033[0m on page \033[31m{pg}\033[0m has been saved.")

    driver.get(f"https://yande.re/post?page=1&tags=rating%3A{rating_str}")
    img_link = driver.find_element(By.XPATH, f'/html/body/div[8]/div[1]/div[2]/div[4]/ul/li[1]/a').get_attribute("href")
    fp = open(f"ai_dataset_2/category_{rating_int}/category_{rating_int}_edge_image_link.txt", 'w')
    fp.write(img_link)
    fp.close()

    pg = 1
    br = False
    while True:
        driver.get(f"https://yande.re/post?page={pg}&tags=rating%3A{rating_str}")
        for i in range(1, 41):
            img_link = driver.find_element(By.XPATH, f'/html/body/div[8]/div[1]/div[2]/div[4]/ul/li[{i}]/a').get_attribute("href")
            if img_link == edge_img_link:
                br = True
                break
            else:
                response = requests.get(img_link)
                if response.status_code:
                    fp = open(f"ai_dataset_2/category_{rating_int}/category_{rating_int}_img_{curr_img_cnt}.jpg", 'wb')
                    fp.write(response.content)
                    fp.close()

                    curr_img_cnt += 1

                print(f"Image \033[31m{i}\033[0m on page \033[31m{pg}\033[0m has been saved.")
        if br:
            break
        pg += 1
except:
    print("Error: try failed while getting newly uploaded images.")

try:
    pg = curr_img_cnt // 40 + 1
    while True:
        driver.get(f"https://yande.re/post?page={pg}&tags=rating%3A{rating_str}")
        for i in range(curr_img_cnt % 40 + 1, 41):
            img_link = driver.find_element(By.XPATH, f'/html/body/div[8]/div[1]/div[2]/div[4]/ul/li[{i}]/a').get_attribute("href")
            response = requests.get(img_link)
            if response.status_code:
                fp = open(f"ai_dataset_2/category_{rating_int}/category_{rating_int}_img_{curr_img_cnt}.jpg", 'wb')
                fp.write(response.content)
                fp.close()

                curr_img_cnt += 1

            print(f"Image \033[31m{i}\033[0m on page \033[31m{pg}\033[0m has been saved.")
        pg += 1
except:
    print("Error: try failed while getting old images.")

driver.quit()

fp = open(f"ai_dataset_2/category_{rating_int}/category_{rating_int}_count.txt", 'w')
fp.write(str(curr_img_cnt))
fp.close()

print("End of program.")