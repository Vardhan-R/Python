from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# driver.get("https://discord.com/app")
# driver.get("https://discord.com/channels/805865687750017045/981153120270827562")
driver.get("https://www.youtube.com/watch?v=e0fcOkvVcDI")

print(driver.title)

# print(driver.title)

# try:
#     email = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.NAME, "email"))
#     )
# except:
#     print("Error: try failed.")
#     driver.quit()
# email.send_keys("email_goes_here")

# password = driver.find_element_by_name("password")
# password.send_keys("password_goes_here")
# password.send_keys(Keys.RETURN)

# try:
#     textbox = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "editor-H2NA06"))
#     )
# except:
#     print("Error: try failed.")
#     driver.quit()

while True:
    try:
        check_pause = driver.find_element(By.CLASS_NAME, "unstarted-mode")
        print("Found")
    except:
        pass

# print("Textbox found.")
# print(textbox.text)

for i in all_msgs:
    print(i.text)

time.sleep(30)

driver.quit()