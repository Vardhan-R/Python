from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image
import numpy as np, requests, time

def intToStr(n: int):
    return chr(-5 * n ** 2 + 3 * n + 115)

rating = 0 # 0 ==> s; 1 ==> q; 2 ==> e

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

fp = open(f"../ai_dataset_2/category_{rating}/category_{rating}_count.txt", 'r')
curr_img_cnt = fp.readline()
fp.close()

try:
    for pg in range(3, 4):
        driver.get(f"https://yande.re/post?page={pg}&tags=rating%3A{intToStr(rating)}")
        # driver.get(f"https://yande.re/post?page={pg}&tags=rating%3As")
        # driver.get(f"https://yande.re/post?page={pg}&tags=rating%3Ae")
        # driver.get(f"https://yande.re/post?page={pg}&tags=rating%3Aq")
        # num_of_imgs = len(WebDriverWait(driver, 30).until(
        #     EC.presence_of_all_elements_located((By.CLASS_NAME, "plid"))
        # ))

        # for i in range(num_of_imgs):
        for i in range(40):
            img_link = driver.find_element(By.XPATH, f'/html/body/div[8]/div[1]/div[2]/div[4]/ul/li[{i + 1}]/a').get_attribute("href")

            # img = Image.open(requests.get(img_link, stream = True, allow_redirects = True).raw)
            # img.save(f"../ai_dataset_2/category_0/category_0_img_{i}.jpg")

            response = requests.get(img_link)
            if response.status_code:
                fp = open(f"../ai_dataset_2/category_{rating}/category_{rating}_img_{40 * (pg - 1) + i}.jpg", 'wb')
                # fp = open(f"../ai_dataset_2/category_0/category_0_img_{40 * (pg - 1) + i}.jpg", 'wb')
                # fp = open(f"../ai_dataset_2/category_1/category_1_img_{40 * (pg - 1) + i}.jpg", 'wb')
                # fp = open(f"../ai_dataset_2/test_images/test_img_{40 * (pg - 1) + i}.jpg", 'wb')
                fp.write(response.content)
                fp.close()

            # print(f"Saved {i + 1} / {num_of_imgs}")
            print(f"Page {pg}; Saved {i + 1} / 40")
except:
    print("Error: try failed while getting images.")

driver.quit()

print("End of program")