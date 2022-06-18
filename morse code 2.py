from pynput.keyboard import Key
from pynput.mouse import Button
from selenium import webdriver
import pynput, time

input_str = "hello".lower()
keyboard = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()
unit_of_tm = 0.1

def dah():
    mouse.press(Button.left)
    time.sleep(3 * unit_of_tm)
    mouse.release(Button.left)
    time.sleep(unit_of_tm)

def dit():
    mouse.press(Button.left)
    time.sleep(unit_of_tm)
    mouse.release(Button.left)
    time.sleep(unit_of_tm)

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
driver.get("https://musiclab.chromeexperiments.com/Spectrogram")

keyboard.press(Key.ctrl)
keyboard.press("w")
keyboard.release("w")
keyboard.release(Key.ctrl)
keyboard.press(Key.cmd)
keyboard.press(Key.up)
keyboard.release(Key.up)
keyboard.release(Key.cmd)
mouse.position = (330, 650)
mouse.click(Button.left)
mouse.position = (700, 420)

time.sleep(3)

for i in input_str:
    if i == "a":
        dit(); dah()
    elif i == "b":
        dah(); dit(); dit(); dit()
    elif i == "c":
        dah(); dit(); dah(); dit()
    elif i == "d":
        dah(); dit(); dit()
    elif i == "e":
        dit()
    elif i == "f":
        dit(); dit(); dah(); dit()
    elif i == "g":
        dah(); dah(); dit()
    elif i == "h":
        dit(); dit(); dit(); dit()
    elif i == "i":
        dit(); dit()
    elif i == "j":
        dit(); dah(); dah(); dah()
    elif i == "k":
        dah(); dit(); dah()
    elif i == "l":
        dit(); dah(); dit(); dit()
    elif i == "m":
        dah(); dah()
    elif i == "n":
        dah(); dit()
    elif i == "o":
        dah(); dah(); dah()
    elif i == "p":
        dit(); dah(); dah(); dit()
    elif i == "q":
        dah(); dah(); dit(); dah()
    elif i == "r":
        dit(); dah(); dit()
    elif i == "s":
        dit(); dit(); dit()
    elif i == "t":
        dah()
    elif i == "u":
        dit(); dit(); dah()
    elif i == "v":
        dit(); dit(); dit(); dah()
    elif i == "w":
        dit(); dah(); dah()
    elif i == "x":
        dah(); dit(); dit(); dah()
    elif i == "y":
        dah(); dit(); dah(); dah()
    elif i == "z":
        dah(); dah(); dit(); dit()
    elif i == " ":
        time.sleep(2 * unit_of_tm)
    elif i == "1":
        dit(); dah(); dah(); dah(); dah()
    elif i == "2":
        dit(); dit(); dah(); dah(); dah()
    elif i == "3":
        dit(); dit(); dit(); dah(); dah()
    elif i == "4":
        dit(); dit(); dit(); dit(); dah()
    elif i == "5":
        dit(); dit(); dit(); dit(); dit()
    elif i == "6":
        dah(); dit(); dit(); dit(); dit()
    elif i == "7":
        dah(); dah(); dit(); dit(); dit()
    elif i == "8":
        dah(); dah(); dah(); dit(); dit()
    elif i == "9":
        dah(); dah(); dah(); dah(); dit()
    elif i == "0":
        dah(); dah(); dah(); dah(); dah()
    elif i == ".":
        dit(); dah(); dit(); dah(); dit(); dah()
    elif i == ",":
        dah(); dah(); dit(); dit(); dah(); dah()
    elif i == "?":
        dit(); dit(); dah(); dah(); dit(); dit()
    elif i == ";":
        dah(); dit(); dah(); dit(); dah(); dit()
    elif i == ":":
        dah(); dah(); dah(); dit(); dit(); dit()
    elif i == "+":
        dit(); dah(); dit(); dah(); dit()
    elif i == "-":
        dah(); dit(); dit(); dit(); dit(); dah()
    elif i == "/":
        dah(); dit(); dit(); dah(); dit()
    elif i == "=":
        dah(); dit(); dit(); dit(); dah()

    time.sleep(2 * unit_of_tm)

time.sleep(5)

driver.quit()