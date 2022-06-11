from pynput.keyboard import Key
from pynput.mouse import Button
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pynput, time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://humanbenchmark.com/tests/aim")

actions = ActionChains(driver)
time.sleep(5)

while True:
    try:
        target = driver.find_element(By.CLASS_NAME, "css-z6vxiy")
        actions.click(target)
        actions.perform()
    except:
        break

time.sleep(30)

driver.quit()

# keyboard = pynput.keyboard.Controller()
# mouse = pynput.mouse.Controller()

# try:
#     target = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "css-1k4dpwl"))
#     )
# except:
#     print("Error: try failed.")
#     driver.quit()

# for i in range(1):
#     target = driver.find_element(By.CLASS_NAME, "css-1k4dpwl")
#     # driver.find_element(By.XPATH, "//div[@class='css-1k4dpwl e6yfngs0']//div[@style='width: 0px; height: 0px; transform: matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 485, 250, 0, 1);']")
#     # target = driver.find_element(By.XPATH, "//div[@class='css-1k4dpwl e6yfngs0'][1]")
#     print(target.style)

# for i in range(31):
#     for j in range(50, 920):
#         for k in range(50, 450):
#             try:
#                 print(j, k)
#                 to_find = "//div[@class='css-1k4dpwl e6yfngs0']//div[@style='width: 0px; height: 0px; transform: matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, " + str(j) + ", " + str(k) + ", 0, 1);']"
#                 driver.find_element(By.XPATH, to_find)
#                 mouse.position = (j, k)
#                 mouse.click(Button.left)
#             except:
#                 pass



# for i in range(100):
#     print(mouse.position)
#     time.sleep(1)
# with keyboard.pressed(Key.ctrl_l):
#     with keyboard.pressed(Key.shift_l):
#         keyboard.press("i")
#         keyboard.release("i")
#         keyboard.press("c")
#         keyboard.release("c")
# mouse.position = (675, 390)
# with keyboard.pressed(Key.ctrl_l):
#     keyboard.press("f")
#     keyboard.release("f")
# keyboard.type("matrix")

# div#"id" "class">div#"id" 
# div#root