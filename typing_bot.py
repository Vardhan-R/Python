from pynput.mouse import Button
from selenium import webdriver
import selenium
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pynput, time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://humanbenchmark.com/tests/typing")

str_to_type = ""
# actions = ActionChains(driver)
keyboard = pynput.keyboard.Controller()

time.sleep(5)

text_to_type = driver.find_elements(By.CLASS_NAME, "incomplete")
total_length = len(text_to_type)
for i in range(total_length):
    if text_to_type[i].text:
        str_to_type += text_to_type[i].text
    else:
        str_to_type += " "
    print(i + 1, "/", total_length)

# actions.send_keys(str_to_type)
# actions.perform()
keyboard.type(str_to_type)

# while True:
#     try:
#         target = driver.find_element(By.CLASS_NAME, "incomplete")
#         if target.text:
#             actions.send_keys(target.text)
#         else:
#             actions.send_keys(Keys.SPACE)
#         actions.perform()
#     except:
#         break

time.sleep(30)

driver.quit()
