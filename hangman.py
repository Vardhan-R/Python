import pygame, random

def draw(n):
    if n == 1:
        for m in range(15):
            print("|")
    elif n == 2:
        print(" " + "_" * 13)
        for m in range(15):
            print("|")
    elif n == 3:
        print(" " + "_" * 13)
        print("|" + " " * 13 + "|")
        for m in range(14):
            print("|")
    elif n == 4:
        print(" " + "_" * 13)
        print("|" + " " * 8 + "_" * 5 + "|" + "_" * 5)
        for m in range(14):
            print("|")
    elif n == 5:
        print(" " + "_" * 13)
        print("|" + " " * 8 + "_" * 5 + "|" + "_" * 5)
        for m in range(5):
            print("|" + " " * 7 + "|")
        for m in range(9):
            print("|")
    elif n == 6:
        print(" " + "_" * 13)
        print("|" + " " * 8 + "_" * 5 + "|" + "_" * 5)
        for m in range(5):
            print("|" + " " * 7 + "|" + " " * 11 + "|")
        for m in range(9):
            print("|")
    elif n == 7:
        print(" " + "_" * 13)
        print("|" + " " * 8 + "_" * 5 + "|" + "_" * 5)
        for m in range(4):
            print("|" + " " * 7 + "|" + " " * 11 + "|")
        print("|" + " " * 7 + "|" + "_" * 11 + "|")
        for m in range(9):
            print("|")
    elif n == 8:
        print(" " + "_" * 13)
        print("|" + " " * 8 + "_" * 5 + "|" + "_" * 5)
        for m in range(4):
            print("|" + " " * 7 + "|" + " " * 11 + "|")
        print("|" + " " * 7 + "|" + "_" * 11 + "|")
        for m in range(5):
            print("|" + " " * 13 + "|")
        for m in range(6):
            print("|")
    elif n == 9:
        print(" " + "_" * 13)
        print("|" + " " * 8 + "_" * 5 + "|" + "_" * 5)
        for m in range(4):
            print("|" + " " * 7 + "|" + " " * 11 + "|")
        print("|" + " " * 7 + "|" + "_" * 11 + "|")
        print("|" + " " * 11 + "/|")
        print("|" + " " * 10 + "/ |")
        print("|" + " " * 9 + "/  |")
        for m in range(2):
            print("|" + " " * 12 + "|")
        for m in range(6):
            print("|")
    elif n == 10:
        print(" " + "_" * 13)
        print("|" + " " * 8 + "_" * 5 + "|" + "_" * 5)
        for m in range(4):
            print("|" + " " * 7 + "|" + " " * 11 + "|")
        print("|" + " " * 7 + "|" + "_" * 11 + "|")
        print("|" + " " * 12 + "/|\\")
        print("|" + " " * 11 + "/ | \\")
        print("|" + " " * 10 + "/  |  \\")
        for m in range(2):
            print("|" + " " * 13 + "|")
        for m in range(6):
            print("|")
    elif n == 11:
        print(" " + "_" * 13)
        print("|" + " " * 8 + "_" * 5 + "|" + "_" * 5)
        for m in range(4):
            print("|" + " " * 7 + "|" + " " * 11 + "|")
        print("|" + " " * 7 + "|" + "_" * 11 + "|")
        print("|" + " " * 12 + "/|\\")
        print("|" + " " * 11 + "/ | \\")
        print("|" + " " * 10 + "/  |  \\")
        for m in range(2):
            print("|" + " " * 13 + "|")
        print("|" + " " * 12 + "/")
        print("|" + " " * 11 + "/")
        print("|" + " " * 10 + "/")
        for m in range(6):
            print("|")
    elif n == 12:
        print(" " + "_" * 13)
        print("|" + " " * 8 + "_" * 5 + "|" + "_" * 5)
        for m in range(4):
            print("|" + " " * 7 + "|" + " " * 11 + "|")
        print("|" + " " * 7 + "|" + "_" * 11 + "|")
        print("|" + " " * 12 + "/|\\")
        print("|" + " " * 11 + "/ | \\")
        print("|" + " " * 10 + "/  |  \\")
        for m in range(2):
            print("|" + " " * 13 + "|")
        print("|" + " " * 12 + "/ \\")
        print("|" + " " * 11 + "/   \\")
        print("|" + " " * 10 + "/     \\")
        for m in range(6):
            print("|")
    elif n == 13:
        print(" " + "_" * 13)
        print("|" + " " * 8 + "_" * 5 + "|" + "_" * 5)
        print("|" + " " * 7 + "|" + " " * 11 + "|")
        print("|" + " " * 7 + "|   X" + " " * 7 + "|")
        for m in range(2):
            print("|" + " " * 7 + "|" + " " * 11 + "|")
        print("|" + " " * 7 + "|" + "_" * 11 + "|")
        print("|" + " " * 12 + "/|\\")
        print("|" + " " * 11 + "/ | \\")
        print("|" + " " * 10 + "/  |  \\")
        for m in range(2):
            print("|" + " " * 13 + "|")
        print("|" + " " * 12 + "/ \\")
        print("|" + " " * 11 + "/   \\")
        print("|" + " " * 10 + "/     \\")
        for m in range(6):
            print("|")
    elif n == 14:
        print(" " + "_" * 13)
        print("|" + " " * 8 + "_" * 5 + "|" + "_" * 5)
        print("|" + " " * 7 + "|" + " " * 11 + "|")
        print("|" + " " * 7 + "|   X   X   |")
        for m in range(2):
            print("|" + " " * 7 + "|" + " " * 11 + "|")
        print("|" + " " * 7 + "|" + "_" * 11 + "|")
        print("|" + " " * 12 + "/|\\")
        print("|" + " " * 11 + "/ | \\")
        print("|" + " " * 10 + "/  |  \\")
        for m in range(2):
            print("|" + " " * 13 + "|")
        print("|" + " " * 12 + "/ \\")
        print("|" + " " * 11 + "/   \\")
        print("|" + " " * 10 + "/     \\")
        for m in range(6):
            print("|")
    else:
        print(" " + "_" * 13)
        print("|" + " " * 8 + "_" * 5 + "|" + "_" * 5)
        print("|" + " " * 7 + "|" + " " * 11 + "|")
        print("|" + " " * 7 + "|   X   X   |")
        print("|" + " " * 7 + "|   _____   |")
        print("|" + " " * 7 + "|" + " " * 7 + "U   |")
        print("|" + " " * 7 + "|" + "_" * 11 + "|")
        print("|" + " " * 12 + "/|\\")
        print("|" + " " * 11 + "/ | \\")
        print("|" + " " * 10 + "/  |  \\")
        for m in range(2):
            print("|" + " " * 13 + "|")
        print("|" + " " * 12 + "/ \\")
        print("|" + " " * 11 + "/   \\")
        print("|" + " " * 10 + "/     \\")
        for m in range(6):
            print("|")

# words = ["baby", "ghost", "kinship", "explain", "commitment", "biscuit", "clarify", "shape", "floor", "mountain", "socialist", "kit", "rear", "hand", "forecast", "draw", "steel", "quarrel", "trust", "hesitate"]

words = ["socialist", "kit", "rear", "hand", "forecast", "draw", "steel", "quarrel", "trust", "hesitate"]
guessed = ""
fails = 0
word = random.choice(words)
for i in word:
    guessed += "_ "
while fails < 15:
    print(guessed)
    if "_" not in guessed: break
    guess = input("Type an alphabet: ").lower()
    if guess not in word:
        fails += 1
        draw(fails)
    else:
        for i in range(len(word)):
            if guess == word[i]:
                guessed = guessed[: 2 * i] + guess.upper() + guessed[2 * i + 1:]
if "_" in guessed:
    print(word.upper())
    print("YOU LOSE!")
else:
    print("YOU WIN!")

# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |

#  _____________
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |

#  _____________
# |             |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |

#  _____________
# |        _____|_____
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |

#  _____________
# |        _____|_____
# |       |
# |       |
# |       |
# |       |
# |       |
# |
# |
# |
# |
# |
# |
# |
# |
# |

#  _____________
# |        _____|_____
# |       |           |
# |       |           |
# |       |           |
# |       |           |
# |       |           |
# |
# |
# |
# |
# |
# |
# |
# |
# |

#  _____________
# |        _____|_____
# |       |           |
# |       |           |
# |       |           |
# |       |           |
# |       |___________|
# |
# |
# |
# |
# |
# |
# |
# |
# |

#  _____________
# |        _____|_____
# |       |           |
# |       |           |
# |       |           |
# |       |           |
# |       |___________|
# |             |
# |             |
# |             |
# |             |
# |             |
# |
# |
# |
# |

#  _____________
# |        _____|_____
# |       |           |
# |       |           |
# |       |           |
# |       |           |
# |       |___________|
# |            /|
# |           / |
# |          /  |
# |             |
# |             |
# |
# |
# |
# |

#  _____________
# |        _____|_____
# |       |           |
# |       |           |
# |       |           |
# |       |           |
# |       |___________|
# |            /|\
# |           / | \
# |          /  |  \
# |             |
# |             |
# |
# |
# |
# |

#  _____________
# |        _____|_____
# |       |           |
# |       |           |
# |       |           |
# |       |           |
# |       |___________|
# |            /|\
# |           / | \
# |          /  |  \
# |             |
# |             |
# |            /
# |           /
# |          /
# |

#  _____________
# |        _____|_____
# |       |           |
# |       |           |
# |       |           |
# |       |           |
# |       |___________|
# |            /|\
# |           / | \
# |          /  |  \
# |             |
# |             |
# |            / \
# |           /   \
# |          /     \
# |

#  _____________
# |        _____|_____
# |       |           |
# |       |   X       |
# |       |           |
# |       |           |
# |       |___________|
# |            /|\
# |           / | \
# |          /  |  \
# |             |
# |             |
# |            / \
# |           /   \
# |          /     \
# |

#  _____________
# |        _____|_____
# |       |           |
# |       |   X   X   |
# |       |           |
# |       |           |
# |       |___________|
# |            /|\
# |           / | \
# |          /  |  \
# |             |
# |             |
# |            / \
# |           /   \
# |          /     \
# |

#  _____________
# |        _____|_____
# |       |           |
# |       |   X   X   |
# |       |   _____   |
# |       |       U   |
# |       |___________|
# |            /|\
# |           / | \
# |          /  |  \
# |             |
# |             |
# |            / \
# |           /   \
# |          /     \
# |