from scipy.fft import fft, fftfreq
import numpy as np, wave
# Number of sample points
N = 600
# sample spacing
T = 1.0 / 800.0

wav_obj = wave.open("C:/Users/vrdhn/Desktop/RPReplay_Final1681723925.wav", 'r')

sample_freq = wav_obj.getframerate()
# print(sample_freq)

n_samples = wav_obj.getnframes()
# print(n_samples)

# t_audio = n_samples/sample_freq
# print(t_audio, "seconds")

signal_wave = wav_obj.readframes(n_samples)
wav_obj.close()

signal_array = np.frombuffer(signal_wave, dtype=np.int16)

# x = np.linspace(0.0, N*T, N, endpoint=False)
x = np.linspace(0, n_samples/sample_freq, num=n_samples)
y = signal_array
yf = fft(y)
xf = fftfreq(N, T)[:N//2]
import matplotlib.pyplot as plt
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()