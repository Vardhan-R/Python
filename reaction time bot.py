from pynput.mouse import Button
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pynput, time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://humanbenchmark.com/tests/reactiontime")

mouse = pynput.mouse.Controller()

for i in range(5):
    try:
        scrn = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "view-go"))
        )
        mouse.click(Button.left)
        time.sleep(3)
        mouse.click(Button.left)
    except:
        print("Error: try failed.")
        driver.quit()

time.sleep(30)

driver.quit()