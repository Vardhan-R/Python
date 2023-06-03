from selenium import webdriver
import matplotlib.pyplot as plt, numpy as np, pyaudio, pynput, struct, time, wave

input_str = "Hello, my name is Vardhan.".lower()
keyboard = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()
unit_of_tm = 0.1
freq = 1000

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
# p = pyaudio.PyAudio()
# wav_obj = wave.open('C:/Users/vrdhn/Desktop/CS/python_files/100Hz_44100Hz_16bit_05sec.wav', 'r')
# wav_obj = wave.open('C:/Users/vrdhn/Desktop/CS/python_files/1kHz_44100Hz_16bit_05sec.wav', 'r')
# wav_obj = wave.open('C:/Users/vrdhn/Desktop/CS/python_files/10kHz_44100Hz_16bit_05sec.wav', 'r')
# one = wav_obj.readframes(int(wav_obj.getframerate() * unit_of_tm))
# wav_obj.close()
# wav_obj = wave.open('C:/Users/vrdhn/Desktop/CS/python_files/zero_kHz.wav', 'r')
# zero = wav_obj.readframes(int(wav_obj.getframerate() * unit_of_tm))
# wav_obj.close()

one_lst = list(2 ** 14 * np.sin(2 * np.pi * freq * np.linspace(0, unit_of_tm, int(RATE * unit_of_tm))))
# print(one_lst[2000:2100])
zero_lst = [0 for _ in range(int(RATE * unit_of_tm))]

# one = "".join(["1" for _ in range(4)])
# zero = "".join(["0" for _ in range(4)])
# one = chr(127)
# zero = chr(0)

# starts recording
# stream = p.open(
#    format=FORMAT,
#    channels=CHANNELS,
#    rate=RATE,
#    input=True,
#    frames_per_buffer=FRAMES_PER_BUFFER
# )

# print("start recording...")

frames = []
# seconds = 1
# for i in range(0, int(RATE / FRAMES_PER_BUFFER * seconds)):
#     data = stream.read(FRAMES_PER_BUFFER)
#     frames.append(data)

# print("recording stopped")

# stream.stop_stream()
# stream.close()
# p.terminate()

def dah():
    global frames

    for _ in range(3):
        frames += one_lst
    frames += zero_lst

    # for i in temp:
    #     i = chr(hex(i))
    # frames.append(b"\xff\xff\xff\x00")
    # frames.append(("".join([one, one, one, zero])).encode("ASCII"))

    # for i in range(3):
    #     for j in one:
    #         frames.append(chr(j).encode())
    # for i in zero:
    #     # frames.append(chr(i).encode())
    #     frames.append(b"\x00")

    # mouse.press(Button.left)
    # time.sleep(3 * unit_of_tm)
    # mouse.release(Button.left)
    # time.sleep(unit_of_tm)

def dit():
    global frames

    frames += one_lst
    frames += zero_lst

    # frames.append(b"\xff\x00")
    # frames.append(("".join([one, zero])).encode("ASCII"))
    # frames += one
    # frames += zero

    # for i in one:
    #     frames.append(chr(i).encode())
    # for i in zero:
    #     # frames.append(chr(i).encode())
    #     frames.append(b"\x00")

    # mouse.press(Button.left)
    # time.sleep(unit_of_tm)
    # mouse.release(Button.left)
    # time.sleep(unit_of_tm)

# driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
# driver.get("https://musiclab.chromeexperiments.com/Spectrogram")

# keyboard.press(Key.ctrl)
# keyboard.press("w")
# keyboard.release("w")
# keyboard.release(Key.ctrl)
# keyboard.press(Key.cmd)
# keyboard.press(Key.up)
# keyboard.release(Key.up)
# keyboard.release(Key.cmd)
# mouse.position = (330, 650)
# mouse.click(Button.left)
# mouse.position = (700, 420)

# time.sleep(3)

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
        frames += zero_lst + zero_lst
        # time.sleep(2 * unit_of_tm)
        # frames.append(b"\x00\x00")
        # frames.append(("".join([zero, zero])).encode("ASCII"))
        # for i in range(2):
        #     for j in zero:
        #         # frames.append(chr(j).encode())
        #         frames.append(b"\x00")
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

    frames += zero_lst + zero_lst
    # time.sleep(2 * unit_of_tm)
    # frames.append(b"\x00\x00")
    # frames.append(("".join([zero, zero])).encode("ASCII"))
    # frames += zero + zero
    # for i in range(2):
    #     for j in zero:
    #         # frames.append(chr(j).encode())
    #         frames.append(b"\x00")

# time.sleep(5)

# for i in range(0xffff):
#     try:
#         chr(i).encode()
#     except:
#         print(i)
#         break

# frames = [chr(i).encode() if i % 2 else chr(1).encode() for i in range(1, 100)]
# frames[127] = chr(1000).encode()

audio_bytes = b"".join(struct.pack("<h", round(i)) for i in frames)
# print(audio_bytes[:100])

# plt.figure(figsize=(10, 5))
# plt.plot(np.arange(np.size(frames)), frames)
# plt.title('Audio')
# plt.ylabel('Signal Value')
# plt.xlabel('Time (s)')
# # plt.xlim(0, t_audio)
# plt.show()

wf = wave.open("output.wav", 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(2)
wf.setframerate(RATE)
# print(len(b''.join(frames[:1])))
# print(frames[0])
wf.writeframes(audio_bytes)
wf.close()

# driver.quit()