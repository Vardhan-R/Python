from built_modules import import_number_system_converter as nsc
from matplotlib import colors, patches, pyplot as plt
import numpy as np

txt_file = open("fav_codes.txt", 'r')
codes = txt_file.readlines()
txt_file.close()

for i in range(len(codes)):
    temp = 16 * int(codes[i][3:-2])
    codes[i] = (temp // 65536 % 256 / 255, temp // 256 % 256 / 255, temp % 256 / 255)

plt.rcParams["figure.figsize"] = (7, 7)
ax = plt.figure().add_subplot()
for i in range(13):
    for j in range(13):
        ax.add_patch(patches.Rectangle((i, j), 1, 1, facecolor=codes[13 * i + j]))
plt.xlim(0, 13)
plt.ylim(0, 13)
plt.show()