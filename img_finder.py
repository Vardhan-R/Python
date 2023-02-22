from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import numpy as np, time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

tags_lst = ["hololive_english", "cum", "gangbang", "bukkake"]
# tags_lst = [""]
tags_len = len(tags_lst)
tags_cnt = []
imgs_lst = []
pg_number = 0

for i in range(tags_len):
    try:
        driver.get(f"https://yande.re/tag?name={tags_lst[i]}&type=&order=count")

        tags_cnt.append(int(WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/table/tbody/tr/td[1]'))
        ).text))
    except:
        print(f"Error: try failed while getting tag counts at i = {i}.")

min_tag_index = np.argmin(np.array(tags_cnt))
tags_cnt.pop(min_tag_index)
min_2_tag_index = np.argmin(np.array(tags_cnt))
if min_2_tag_index >= min_tag_index:
    min_2_tag_index += 1
min_tags = f"{tags_lst[min_tag_index]}+{tags_lst[min_2_tag_index]}"

# try:
    # driver.get("https://yande.re/post")
# except:
#     print("Try failed while getting images.")

# print(tags_cnt)

# driver.quit()

try:
    # search
    # driver.get("https://yande.re/post")

    # search = WebDriverWait(driver, 30).until(
    #     EC.presence_of_element_located((By.ID, "tags"))
    # )

    # search.send_keys(f"{tags_lst[min_tag_index]} {tags_lst[min_2_tag_index]}\n")

    # search.send_keys("bukkake gangbang\n")
    # driver.get(f"https://yande.re/post?tags={tags_lst[min_tag_index]}+{tags_lst[min_2_tag_index]}")
    while True:
        pg_number += 1
        driver.get(f"https://yande.re/post?page={pg_number}&tags={min_tags}")

        # all_imgs_on_pg = WebDriverWait(driver, 30).until(
        #     EC.presence_of_all_elements_located((By.CLASS_NAME, "thumb"))
        # )
        num_of_imgs = len(WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "plid"))
        ))

        for i in range(num_of_imgs):
            img_tags = driver.find_element(By.XPATH, f'/html/body/div[8]/div[1]/div[2]/div[4]/ul/li[{i + 1}]/div/a/img').get_attribute("alt")
            allowed = True
            for j in tags_lst:
                if j not in img_tags:
                    allowed = False
                    break
            if allowed:
                imgs_lst.append(driver.find_element(By.XPATH, f'/html/body/div[8]/div[1]/div[2]/div[4]/ul/li[{i + 1}]/div/a').get_attribute("href")[27:])

        if driver.find_element(By.CLASS_NAME, "next_page").get_attribute("rel") != "next":
            print("All pages done.")
            break

    # all_imgs_links = []
    # print(driver.find_elements(By.XPATH, '/html/head/title')[0].text)
    # print(driver.find_element(By.CSS_SELECTOR, ""))
    # for i in range(1):
    #     all_imgs_links.append(driver.find_element(By.XPATH, f'/html/body/div[8]/div[1]/div[2]/div[4]/ul/li[{i + 1}]/div/a/span'))
    # all_imgs_on_pg = WebDriverWait(driver, 30).until(
    #     EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[8]/div[1]/div[2]/div[4]/ul/li[1]/div/a/span'))
    # )

    # print(all_imgs_links[0].text)

    # hidden_imgs = driver.find_elements(By.CLASS_NAME, "no-focus-outline")
    # for j in hidden_imgs:
    #     j.click()

    # for i in all_imgs_on_pg:
        # print(i.text[4:])
        # '//*[@id="p1056650"]/div/a/span'
        # '/html/body/div[8]/div[1]/div[2]/div[4]/ul/li[1]/div/a/span'
        # '/html/body/div[8]/div[1]/div[2]/div[4]/ul/li[2]/div/a/span'
        # all_imgs_links.append(i.text[4:])

    # for i in all_imgs_links:
    #     driver.get(i)
    #     img_tags = WebDriverWait(driver, 30).until(
    #         EC.presence_of_all_elements_located((By.ID, "post_tags"))
    #     ).text
    #     allowed = True
    #     for j in tags_lst:
    #         if j not in img_tags:
    #             allowed = False
    #             break
    #     if allowed:
            # imgs_lst.append(i[27:])

    # for i in range(num_of_imgs):
    # # for i in range(1):
    #     all_imgs_on_pg = WebDriverWait(driver, 30).until(
    #         EC.presence_of_all_elements_located((By.CLASS_NAME, "thumb"))
    #     )
    #     hidden_imgs = driver.find_elements(By.CLASS_NAME, "no-focus-outline")
    #     for j in hidden_imgs:
    #         j.click()
    #     all_imgs_on_pg[i].click()
    #     # driver.get("https://yande.re/post/show/1056650")

    #     WebDriverWait(driver, 30).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "js-posts-show-edit-tab"))
    #     ).click()
    #     # edit_link.click()

    #     time.sleep(0.5)
    #     img_tags = driver.find_element(By.ID, "post_tags").text
    #     allowed = True
    #     for j in tags_lst:
    #         if j not in img_tags:
    #             allowed = False
    #             break
    #     if allowed:
    #         imgs_lst.append(driver.find_element(By.XPATH, '//*[@id="stats"]/ul/li[1]').text[4:])

    #     driver.back()

    #     time.sleep(3)
        # ['1050709', '1050707', '1050705', '1050704', '1050681', '1050680']

    # print(tags_link.tag_name)

    # tags_link = WebDriverWait(driver, 30).until(
    #     EC.presence_of_all_elements_located((By.TAG_NAME, "align"))
    # )

    # search.send_keys("mmf uncensored nakadashi paizuri\n")

    # popular_all_time = WebDriverWait(driver, 30).until(
    #     EC.presence_of_element_located((By.LINK_TEXT, "all time"))
    # )
    # popular_all_time.click()

    # while True:
    #     pg_number += 1

    #     hentai_links_lst = WebDriverWait(driver, 30).until(
    #         EC.presence_of_all_elements_located((By.CLASS_NAME, "lazyload"))
    #     )
    #     total_hentai_cnt = len(hentai_links_lst)

    #     for i in range(total_hentai_cnt):
    #         allowed = True
    #         j = 0

    #         hentai_links_lst = WebDriverWait(driver, 30).until(
    #             EC.presence_of_all_elements_located((By.CLASS_NAME, "lazyload"))
    #         )
    #         hentai_links_lst[i].click()

    #         while allowed:
    #             j += 1
    #             try:
    #                 tag = driver.find_element(By.XPATH, '//*[@id="tags"]/div[3]/span/a[' + str(j) + ']/span[1]')
    #                 if tag.text in ["futanari", "lolicon"]:
    #                     allowed = False
    #             except:
    #                 break

    #         if allowed:
    #             codes_file = open("codes.txt", 'a')
    #             codes_file.write(driver.find_element(By.ID, "gallery_id").text + '\n')
    #             codes_file.close()
    #             print("Page number:", str(pg_number) + ";", i + 1, "/", str(total_hentai_cnt) + ";", "saved")
    #         else:
    #             print("Page number:", str(pg_number) + ";", i + 1, "/", str(total_hentai_cnt) + ";", "not saved")

    #         driver.back()

    #     try:
    #         nxt_pg_button = WebDriverWait(driver, 5).until(
    #             EC.presence_of_element_located((By.CLASS_NAME, "next"))
    #         )
    #         nxt_pg_button.click()
    #     except:
    #         break
except:
    print("Error: try failed while getting images.")

print(imgs_lst)

driver.quit()