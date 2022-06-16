from pynput.mouse import Button
import pynput, time

input_str = "hello".lower()
mouse = pynput.mouse.Controller()
unit_of_tm = 0.1

def d():
    mouse.press(Button.left)
    time.sleep(unit_of_tm)
    mouse.release(Button.left)
    time.sleep(unit_of_tm)

def D():
    mouse.press(Button.left)
    time.sleep(3 * unit_of_tm)
    mouse.release(Button.left)
    time.sleep(unit_of_tm)

time.sleep(10)
mouse.position = (700, 420)

for i in input_str:
    if i == "a":
        d(); D()
    elif i == "b":
        D(); d(); d(); d()
    elif i == "c":
        D(); d(); D(); d()
    elif i == "d":
        D(); d(); d()
    elif i == "e":
        d()
    elif i == "f":
        d(); d(); D(); d()
    elif i == "g":
        D(); D(); d()
    elif i == "h":
        d(); d(); d(); d()
    elif i == "i":
        d(); d()
    elif i == "j":
        d(); D(); D(); D()
    elif i == "k":
        D(); d(); D()
    elif i == "l":
        d(); D(); d(); d()
    elif i == "m":
        D(); D()
    elif i == "n":
        D(); d()
    elif i == "o":
        D(); D(); D()
    elif i == "p":
        d(); D(); D(); d()
    elif i == "q":
        D(); D(); d(); D()
    elif i == "r":
        d(); D(); d()
    elif i == "s":
        d(); d(); d()
    elif i == "t":
        D()
    elif i == "u":
        d(); d(); D()
    elif i == "v":
        d(); d(); d(); D()
    elif i == "w":
        d(); D(); D()
    elif i == "x":
        D(); d(); d(); D()
    elif i == "y":
        D(); d(); D(); D()
    elif i == "z":
        D(); D(); d(); d()
    elif i == " ":
        time.sleep(2 * unit_of_tm)
    elif i == "1":
        d(); D(); D(); D(); D()
    elif i == "2":
        d(); d(); D(); D(); D()
    elif i == "3":
        d(); d(); d(); D(); D()
    elif i == "4":
        d(); d(); d(); d(); D()
    elif i == "5":
        d(); d(); d(); d(); d()
    elif i == "6":
        D(); d(); d(); d(); d()
    elif i == "7":
        D(); D(); d(); d(); d()
    elif i == "8":
        D(); D(); D(); d(); d()
    elif i == "9":
        D(); D(); D(); D(); d()
    elif i == "0":
        D(); D(); D(); D(); D()
    elif i == ".":
        d(); D(); d(); D(); d(); D()
    elif i == ",":
        D(); D(); d(); d(); D(); D()
    elif i == "?":
        d(); d(); D(); D(); d(); d()
    elif i == ";":
        D(); d(); D(); d(); D(); d()
    elif i == ":":
        D(); D(); D(); d(); d(); d()
    elif i == "+":
        d(); D(); d(); D(); d()
    elif i == "-":
        D(); d(); d(); d(); d(); D()
    elif i == "/":
        D(); d(); d(); D(); d()
    elif i == "=":
        D(); d(); d(); d(); D()

    time.sleep(2 * unit_of_tm)