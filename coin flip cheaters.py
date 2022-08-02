import random
import matplotlib.pyplot as plt
import numpy as np

threshold_h = 6
threshold_t = 4
games = 1000
all_scores = np.empty(games, int)

for i in range(games):
    flips = 100
    score = 0

    while flips > 0:
        h = 0
        t = 0
        player = random.choice(["fair", "cheater"])
        while True:
            if h >= threshold_h:
                if player == "cheater":
                    flips += 15
                    score += 1
                else:
                    flips -= 30
                break
            elif t >= threshold_t:
                if player == "fair":
                    flips += 15
                    score += 1
                else:
                    flips -= 30
                break
            else:
                if player == "fair":
                    flip = random.choice(["H", "T"])
                else:
                    flip = random.choice(["H", "H", "H", "T"])
                flips -= 1
                if flip == "H":
                    h += 1
                else:
                    t += 1
    all_scores[i] = score
# print(all_scores)
print(np.average(all_scores))
# all_scores = np.arange(9)
freqs_and_scores = np.histogram(all_scores, bins=np.arange(np.amax(all_scores) + 2))
# print(freqs_and_scores[0])
# print(freqs_and_scores[1])
# print(len(freqs_and_scores[0]))
# print(len(freqs_and_scores[1]))
plt.bar(freqs_and_scores[1][:-1], freqs_and_scores[0])
plt.xlim([0, np.amax(all_scores) + 1])
plt.show()
