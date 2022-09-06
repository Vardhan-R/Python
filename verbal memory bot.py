from pynput.mouse import Button
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import pynput, time

word_lst = []

PATH = "D:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://humanbenchmark.com/tests/verbal-memory")

mouse = pynput.mouse.Controller()

time.sleep(5)

while len(word_lst) < 1000:
    try:
        word = driver.find_element(By.CLASS_NAME, "word")
        current_word = word.text
        temp = driver.find_elements(By.CLASS_NAME, "e19owgy710")
        if current_word in word_lst:
            temp[0].click()
        else:
            word_lst.append(current_word)
            temp[1].click()
    except:
        print("Error: try failed.")
        break

time.sleep(30)

driver.quit()
