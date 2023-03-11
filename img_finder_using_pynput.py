from pynput.mouse import Button
import pynput, time

rating_str = "s"

keyboard = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()

time.sleep(2)

for pg in range(1, 4):
    # go to page
    mouse.position = (400, 52)
    mouse.click(Button.left, 1)
    time.sleep(0.1)
    keyboard.type(f"https://yande.re/post?page={pg}&tags=rating%3A{rating_str}\n")
    time.sleep(1)

    # open extension and save images
    mouse.position = (2407, 52)
    mouse.click(Button.left, 1)
    time.sleep(0.1)
    mouse.position = (2233, 238)
    mouse.click(Button.left, 1)
    time.sleep(0.5)
    mouse.position = (1960, 218)
    mouse.click(Button.left, 1)
    time.sleep(0.1)
    mouse.position = (2318, 633)
    mouse.click(Button.left, 1)
    time.sleep(0.1)