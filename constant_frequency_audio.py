import matplotlib.pyplot as plt, numpy as np, pyaudio, pynput, struct, time, wave

input_str = "Hello, my name is Vardhan.".lower()
keyboard = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()
tm = 5
freq_1 = 349.2282
freq_2 = freq_1 * 2 ** (1 / 3)
freq_3 = freq_2 * 2 ** (1 / 4)

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

temp_arr = 2 * np.pi * np.linspace(0, tm, int(RATE * tm))

# frames = list(2 ** 14 / 3 * (np.sin(temp_arr * freq_1)
#                        + np.sin(temp_arr * freq_2))
#                        + np.sin(temp_arr * freq_3))

frames = list(2 ** 13 * (-np.sin(3 * 440 * temp_arr) / 4 + np.sin(440 * temp_arr) / 4 + np.sqrt(3) * np.cos(440 * temp_arr) / 2))

audio_bytes = b"".join(struct.pack("<h", round(i)) for i in frames)

wf = wave.open("output.wav", 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(2)
wf.setframerate(RATE)
# print(len(b''.join(frames[:1])))
# print(frames[0])
wf.writeframes(audio_bytes)
wf.close()