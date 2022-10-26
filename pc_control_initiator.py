from pynput.mouse import Button
import pynput, time

mouse = pynput.mouse.Controller()

while True:
    mouse.position = (1014, 906)
    time.sleep(0.1)
    mouse.click(Button.left, 1)
    time.sleep(3)
    mouse.position = (1085, 705)
    time.sleep(0.1)
    mouse.click(Button.left, 1)
    time.sleep(3)
    mouse.position = (1094, 845)
    time.sleep(0.1)
    mouse.click(Button.left, 1)
    time.sleep(10)
