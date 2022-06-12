from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

pg_number = 0

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://nhentai.net")

try:
    search = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/nav/form/input"))
    )
    # search.send_keys("mmf uncensored\n")
    # search.send_keys("nakadashi shotacon paizuri\n")
    search.send_keys("mmf uncensored nakadashi paizuri\n")
    # search.send_keys("mmf uncensored shotacon nakadashi paizuri\n")

    popular_all_time = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.LINK_TEXT, "all time"))
    )
    popular_all_time.click()

    while True:
        pg_number += 1

        hentai_links_lst = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "lazyload"))
        )
        total_hentai_cnt = len(hentai_links_lst)

        for i in range(total_hentai_cnt):
            allowed = True
            j = 0

            hentai_links_lst = WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "lazyload"))
            )
            hentai_links_lst[i].click()

            while allowed:
                j += 1
                try:
                    tag = driver.find_element(By.XPATH, '//*[@id="tags"]/div[3]/span/a[' + str(j) + ']/span[1]')
                    if tag.text in ["futanari", "lolicon"]:
                        allowed = False
                except:
                    break

            if allowed:
                codes_file = open("Vardhan/codes.txt", 'a')
                codes_file.write(driver.find_element(By.ID, "gallery_id").text + '\n')
                codes_file.close()
                print("Page number:", str(pg_number) + ";", i + 1, "/", str(total_hentai_cnt) + ";", "saved")
            else:
                print("Page number:", str(pg_number) + ";", i + 1, "/", str(total_hentai_cnt) + ";", "not saved")

            driver.back()

        try:
            nxt_pg_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "next"))
            )
            nxt_pg_button.click()
        except:
            break
except:
    print("Error: try failed.")

driver.quit()
