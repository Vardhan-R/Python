from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# driver.get("https://youtube.com")
# print(driver.title)
# tab_1 = driver.current_window_handle
# driver.execute_script("window.open('about:blank', 'tab_2');")

# time.sleep(5)

# first_tab = driver.title
# print(first_tab)

# driver.switch_to.window("tab_2")
driver.get("https://www.youtube.com/watch?v=e0fcOkvVcDI")

print(driver.title)

# time.sleep(5)

# search = driver.find_element_by_name("search_query")
# search.send_keys("abc")
# search.send_keys(Keys.RETURN)


for i in range(100):
    time.sleep(1)
    search = driver.find_element_by_class_name("ytp-time-current")
    print(search.text)

# i = 0
# while driver.title != first_tab:
#     driver.switch_to.window(driver.window_handles[i])
#     i += 1

# print(driver.title)

# search = driver.find_element_by_name("search_query")
# search.send_keys("abc")
# search.send_keys(Keys.RETURN)

time.sleep(30)

driver.quit()