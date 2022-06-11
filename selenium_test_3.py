from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# driver.get("https://discord.com/app")
driver.get("https://discord.com/channels/805865687750017045/981153120270827562")

try:
    email = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
except:
    print("Error: try failed.")
    driver.quit()
email.send_keys("email_goes_here")

password = driver.find_element_by_name("password")
password.send_keys("password_goes_here")
password.send_keys(Keys.RETURN)

time.sleep(5)

driver.execute_script("window.open('about:blank', 'tab_2');")
discord_title = driver.title

driver.switch_to.window("tab_2")
driver.get("https://www.youtube.com/watch?v=i83ZUAmOi5s")
yt_title = driver.title

for i in range(3):
    time.sleep(0.5)
    search = driver.find_element_by_class_name("ytp-time-current")
    timestamp = search.text

    j = 0
    while driver.title != discord_title:
        driver.switch_to.window(driver.window_handles[j])
        j += 1

    try:
        textbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "editor-H2NA06"))
        )
    except:
        print("Error: try failed.")
        driver.quit()

    textbox.send_keys(timestamp + '\n')

    j = 0
    while driver.title != yt_title:
        driver.switch_to.window(driver.window_handles[j])
        j += 1

j = 0
while driver.title != discord_title:
    driver.switch_to.window(driver.window_handles[j])
    j += 1

try:
    all_msgs = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "markup-eYLPri"))
    )
except:
    print("Error: try failed.")
    driver.quit()

print(all_msgs[-2].text)

time.sleep(30)

driver.quit()