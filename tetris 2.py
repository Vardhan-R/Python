import math, pygame, random, time

pygame.init()

width = 250
height = 600
running = True
black = (0, 0, 0)
grey = (128, 128, 128)
white = (255, 255, 255)
red = (255, 0, 0) # Z1
green = (0, 255, 0) # S2
blue = (0, 0, 255) # J3
orange = (255, 128, 0) # L4
yellow = (255, 255, 0) # O5
magenta = (255, 0, 255) # T6
cyan = (0, 255, 255) # I7
rows = 24 # total
blank_rows = 4
cols = 10
t = 0
board = []
temp_lst = []

for i in range(cols):
    temp_lst.append(0)
for i in range(rows):
    board.append(temp_lst.copy())

scrn = pygame.display.set_mode((width, height))

class BlockZ:
    def __init__(self):
        self.pos = [[blank_rows, 3], [blank_rows, 4], [blank_rows + 1, 4], [blank_rows + 1, 5]]
        for i in self.pos:
            board[i[0]][i[1]] = 1
        self.kind = 1
        self.orientation = 1
        self.bottoms = [0, 2, 3]
        self.lefts = [0, 2]
        self.rights = [1, 3]

    def rotate(self, dir):
        for i in self.pos:
            board[i[0]][i[1]] = 0
        if dir == "cw":
            if self.orientation == 1:
                self.pos[0][1] += 2
                self.pos[1][0] += 1
                self.pos[2][1] += 1
                self.pos[3][0] += 1
                self.pos[3][1] -= 1
                self.orientation = 2
            elif self.orientation == 2:
                self.pos[0][0] += 1
                self.pos[0][1] -= 2
                self.pos[2][0] += 1
                self.pos[2][1] -= 1
                self.pos[3][1] += 1
                self.orientation = 3
            elif self.orientation == 3:
                self.pos[0][0] -= 1
                self.pos[0][1] += 1
                self.pos[1][1] -= 1
                self.pos[2][0] -= 1
                self.pos[3][1] -= 2
                self.orientation = 4
            else:
                self.pos[0][1] -= 1
                self.pos[1][0] -= 1
                self.pos[1][1] += 1
                self.pos[3][0] -= 1
                self.pos[3][1] += 2
                self.orientation = 1
        else:
            if self.orientation == 1:
                self.pos[0][1] += 1
                self.pos[1][0] += 1
                self.pos[1][1] -= 1
                self.pos[3][0] += 1
                self.pos[3][1] -= 2
                self.orientation = 4
            elif self.orientation == 2:
                self.pos[0][1] -= 2
                self.pos[1][0] -= 1
                self.pos[2][1] -= 1
                self.pos[3][0] -= 1
                self.pos[3][1] += 1
                self.orientation = 1
            elif self.orientation == 3:
                self.pos[0][0] -= 1
                self.pos[0][1] += 2
                self.pos[2][0] -= 1
                self.pos[2][1] += 1
                self.pos[3][1] -= 1
                self.orientation = 2
            else:
                self.pos[0][0] += 1
                self.pos[0][1] -= 1
                self.pos[1][1] += 1
                self.pos[2][0] += 1
                self.pos[3][1] += 2
                self.orientation = 3
        for i in self.pos:
            board[i[0]][i[1]] = 1

    def update(self):
        if self.orientation in [1, 3]:
            self.lefts = [0, 2]
            self.rights = [1, 3]
        else:
            self.lefts = [1, 3]
            self.rights = [0, 2]

class BlockS:
    def __init__(self):
        self.pos = [[blank_rows, 4], [blank_rows, 5], [blank_rows + 1, 3], [blank_rows + 1, 4]]
        for i in self.pos:
            board[i[0]][i[1]] = 2
        self.kind = 2
        self.orientation = 1
        self.bottoms = [1, 2, 3]
        self.lefts = [0, 2]
        self.rights = [1, 3]

    def rotate(self, dir):
        for i in self.pos:
            board[i[0]][i[1]] = 0
        if dir == "cw":
            if self.orientation == 1:
                self.pos[1][0] += 1
                self.pos[1][1] -= 1
                self.pos[2][1] += 2
                self.pos[3][0] += 1
                self.pos[3][1] += 1
                self.orientation = 2
            elif self.orientation == 2:
                self.pos[0][0] += 1
                self.pos[1][1] += 1
                self.pos[2][0] += 1
                self.pos[2][1] -= 2
                self.pos[3][1] -= 1
                self.orientation = 3
            elif self.orientation == 3:
                self.pos[0][0] -= 1
                self.pos[0][1] -= 1
                self.pos[1][1] -= 2
                self.pos[2][0] -= 1
                self.pos[2][1] += 1
                self.orientation = 4
            else:
                self.pos[0][1] += 1
                self.pos[1][0] -= 1
                self.pos[1][1] += 2
                self.pos[2][1] -= 1
                self.pos[3][0] -= 1
                self.orientation = 1
        else:
            if self.orientation == 1:
                self.pos[0][1] -= 1
                self.pos[1][0] += 1
                self.pos[1][1] -= 2
                self.pos[2][1] += 1
                self.pos[3][0] += 1
                self.orientation = 4
            elif self.orientation == 2:
                self.pos[1][0] -= 1
                self.pos[1][1] += 1
                self.pos[2][1] -= 2
                self.pos[3][0] -= 1
                self.pos[3][1] -= 1
                self.orientation = 1
            elif self.orientation == 3:
                self.pos[0][0] -= 1
                self.pos[1][1] -= 1
                self.pos[2][0] -= 1
                self.pos[2][1] += 2
                self.pos[3][1] += 1
                self.orientation = 2
            else:
                self.pos[0][0] += 1
                self.pos[0][1] += 1
                self.pos[1][1] += 2
                self.pos[2][0] += 1
                self.pos[2][1] -= 1
                self.orientation = 3
        for i in self.pos:
            board[i[0]][i[1]] = 2

    def update(self):
        if self.orientation in [1, 3]:
            self.lefts = [0, 2]
            self.rights = [1, 3]
        else:
            self.lefts = [0, 1]
            self.rights = [2, 3]

class BlockJ:
    def __init__(self):
        self.pos = [[blank_rows, 3], [blank_rows, 4], [blank_rows, 5], [blank_rows + 1, 5]]
        for i in self.pos:
            board[i[0]][i[1]] = 3
        self.kind = 3
        self.orientation = 1
        self.bottoms = [0, 1, 3]
        self.lefts = [0, 3]
        self.rights = [2, 3]

    def rotate(self, dir):
        for i in self.pos:
            board[i[0]][i[1]] = 0
        if dir == "cw":
            if self.orientation == 1:
                self.pos[0][0] -= 1
                self.pos[0][1] += 1
                self.pos[2][0] += 1
                self.pos[2][1] -= 1
                self.pos[3][1] -= 2
                self.orientation = 2
            elif self.orientation == 2:
                self.pos[0][1] -= 1
                self.pos[1][1] -= 1
                self.pos[2][0] -= 1
                self.pos[3][0] -= 1
                self.pos[3][1] += 2
                self.orientation = 3
            elif self.orientation == 3:
                self.pos[0][1] += 1
                self.pos[1][0] -= 1
                self.pos[1][1] += 2
                self.pos[3][0] += 1
                self.pos[3][1] -= 1
                self.orientation = 4
            else:
                self.pos[0][0] += 1
                self.pos[0][1] -= 1
                self.pos[1][0] += 1
                self.pos[1][1] -= 1
                self.pos[2][1] += 1
                self.pos[3][1] += 1
                self.orientation = 1
        else:
            if self.orientation == 1:
                self.pos[0][0] -= 1
                self.pos[0][1] += 1
                self.pos[1][0] -= 1
                self.pos[1][1] += 1
                self.pos[2][1] -= 1
                self.pos[3][1] -= 1
                self.orientation = 4
            elif self.orientation == 2:
                self.pos[0][0] += 1
                self.pos[0][1] -= 1
                self.pos[2][0] -= 1
                self.pos[2][1] += 1
                self.pos[3][1] += 2
                self.orientation = 1
            elif self.orientation == 3:
                self.pos[0][1] += 1
                self.pos[1][1] += 1
                self.pos[2][0] += 1
                self.pos[3][0] += 1
                self.pos[3][1] -= 2
                self.orientation = 2
            else:
                self.pos[0][1] -= 1
                self.pos[1][0] += 1
                self.pos[1][1] -= 2
                self.pos[3][0] -= 1
                self.pos[3][1] += 1
                self.orientation = 3
        for i in self.pos:
            board[i[0]][i[1]] = 3

    def update(self):
        if self.orientation == 1:
            self.bottoms = [0, 1, 3]
            self.lefts = [0, 3]
            self.rights = [2, 3]
        elif self.orientation == 2:
            self.bottoms == [2, 3]
            self.lefts = [0, 1, 2]
            self.rights = [0, 1, 3]
        elif self.orientation == 3:
            self.bottoms = [1, 2, 3]
            self.lefts = [0, 1]
            self.rights = [0, 3]
        else:
            self.bottoms = [1, 3]
            self.lefts = [0, 2, 3]
            self.rights = [1, 2, 3]

class BlockL:
    def __init__(self):
        self.pos = [[blank_rows, 3], [blank_rows, 4], [blank_rows, 5], [blank_rows + 1, 3]]
        for i in self.pos:
            board[i[0]][i[1]] = 4
        self.kind = 4
        self.orientation = 1
        self.bottoms = [1, 2, 3]
        self.lefts = [0, 3]
        self.rights = [2, 3]

    def rotate(self, dir):
        for i in self.pos:
            board[i[0]][i[1]] = 0
        if dir == "cw":
            if self.orientation == 1:
                self.pos[0][0] -= 1
                self.pos[1][0] -= 1
                self.pos[2][1] -= 1
                self.pos[3][1] += 1
                self.orientation = 2
            elif self.orientation == 2:
                self.pos[0][1] += 2
                self.pos[1][0] += 1
                self.pos[1][1] -= 1
                self.pos[3][0] -= 1
                self.pos[3][1] += 1
                self.orientation = 3
            elif self.orientation == 3:
                self.pos[0][1] -= 1
                self.pos[1][1] += 1
                self.pos[2][0] += 1
                self.pos[3][0] += 1
                self.orientation = 4
            else:
                self.pos[0][0] += 1
                self.pos[0][1] -= 1
                self.pos[2][0] -= 1
                self.pos[2][1] += 1
                self.pos[3][1] -= 2
                self.orientation = 1
        else:
            if self.orientation == 1:
                self.pos[0][0] -= 1
                self.pos[0][1] += 1
                self.pos[2][0] += 1
                self.pos[2][1] -= 1
                self.pos[3][1] += 2
                self.orientation = 4
            elif self.orientation == 2:
                self.pos[0][0] += 1
                self.pos[1][0] += 1
                self.pos[2][1] += 1
                self.pos[3][1] -= 1
                self.orientation = 1
            elif self.orientation == 3:
                self.pos[0][1] -= 2
                self.pos[1][0] -= 1
                self.pos[1][1] += 1
                self.pos[3][0] += 1
                self.pos[3][1] -= 1
                self.orientation = 2
            else:
                self.pos[0][1] += 1
                self.pos[1][1] -= 1
                self.pos[2][0] -= 1
                self.pos[3][0] -= 1
                self.orientation = 3
        for i in self.pos:
            board[i[0]][i[1]] = 4

    def update(self):
        if self.orientation == 1:
            self.bottoms = [1, 2, 3]
            self.lefts = [0, 3]
            self.rights = [2, 3]
        elif self.orientation == 2:
            self.bottoms == [0, 2, 3]
            self.lefts = [0, 2, 3]
            self.rights = [1, 2, 3]
        elif self.orientation == 3:
            self.bottoms = [1, 2, 3]
            self.lefts = [0, 1]
            self.rights = [0, 3]
        else:
            self.bottoms = [2, 3]
            self.lefts = [0, 1, 2]
            self.rights = [0, 1, 3]

class BlockO:
    def __init__(self):
        self.pos = [[blank_rows, 4], [blank_rows, 5], [blank_rows + 1, 4], [blank_rows + 1, 5]]
        for i in self.pos:
            board[i[0]][i[1]] = 5
        self.kind = 5
        self.bottoms = [2, 3]
        self.lefts = [0, 2]
        self.rights = [1, 3]

    def rotate(self, dir):
        pass

    def update(self):
        pass

class BlockT:
    def __init__(self):
        self.pos = [[blank_rows, 3], [blank_rows, 4], [blank_rows, 5], [blank_rows + 1, 4]]
        for i in self.pos:
            board[i[0]][i[1]] = 6
        self.kind = 6
        self.orientation = 1
        self.bottoms = [0, 2, 3]
        self.lefts = [0, 3]
        self.rights = [2, 3]

    def rotate(self, dir):
        for i in self.pos:
            board[i[0]][i[1]] = 0
        if dir == "cw":
            if self.orientation == 1:
                self.pos[0][0] -= 1
                self.pos[0][1] += 1
                self.pos[1][1] -= 1
                self.pos[2][1] -= 1
                self.orientation = 2
            elif self.orientation == 2:
                self.pos[3][0] -= 1
                self.pos[3][1] += 1
                self.orientation = 3
            elif self.orientation == 3:
                self.pos[1][1] += 1
                self.pos[2][1] += 1
                self.pos[3][0] += 1
                self.pos[3][1] -= 1
                self.orientation = 4
            else:
                self.pos[0][0] += 1
                self.pos[0][1] -= 1
                self.orientation = 1
        else:
            if self.orientation == 1:
                self.pos[0][0] -= 1
                self.pos[0][1] += 1
                self.orientation = 4
            elif self.orientation == 2:
                self.pos[0][0] += 1
                self.pos[0][1] -= 1
                self.pos[1][1] += 1
                self.pos[2][1] += 1
                self.orientation = 1
            elif self.orientation == 3:
                self.pos[3][0] += 1
                self.pos[3][1] -= 1
                self.orientation = 2
            else:
                self.pos[1][1] -= 1
                self.pos[2][1] -= 1
                self.pos[3][0] -= 1
                self.pos[3][1] += 1
                self.orientation = 3
        for i in self.pos:
            board[i[0]][i[1]] = 6

    def update(self):
        if self.orientation == 1:
            self.bottoms = [0, 2, 3]
            self.lefts = [0, 3]
            self.rights = [2, 3]
        elif self.orientation == 2:
            self.bottoms == [1, 3]
            self.lefts = [0, 1, 3]
            self.rights = [0, 2, 3]
        elif self.orientation == 3:
            self.bottoms = [1, 2, 3]
            self.lefts = [0, 1]
            self.rights = [0, 3]
        else:
            self.bottoms = [2, 3]
            self.lefts = [0, 1, 3]
            self.rights = [0, 2, 3]

class BlockI:
    def __init__(self):
        self.pos = [[blank_rows, 3], [blank_rows, 4], [blank_rows, 5], [blank_rows, 6]]
        for i in self.pos:
            board[i[0]][i[1]] = 7
        self.kind = 7
        self.orientation = 1
        self.bottoms = [0, 1, 2, 3]
        self.lefts = [0]
        self.rights = [3]

    def rotate(self, dir):
        for i in self.pos:
            board[i[0]][i[1]] = 0
        if dir == "cw":
            if self.orientation == 1:
                self.pos[0][0] -= 1
                self.pos[0][1] += 2
                self.pos[1][1] += 1
                self.pos[2][0] += 1
                self.pos[3][0] += 2
                self.pos[3][1] -= 1
                self.orientation = 2
            elif self.orientation == 2:
                self.pos[0][0] += 2
                self.pos[0][1] -= 2
                self.pos[1][0] += 1
                self.pos[1][1] -= 1
                self.pos[3][0] -= 1
                self.pos[3][1] += 1
                self.orientation = 3
            elif self.orientation == 3:
                self.pos[0][0] -= 2
                self.pos[0][1] += 1
                self.pos[1][0] -= 1
                self.pos[2][1] -= 1
                self.pos[3][0] += 1
                self.pos[3][1] -= 2
                self.orientation = 4
            else:
                self.pos[0][0] += 1
                self.pos[0][1] -= 1
                self.pos[2][0] -= 1
                self.pos[2][1] += 1
                self.pos[3][0] -= 2
                self.pos[3][1] += 2
                self.orientation = 1
        else:
            if self.orientation == 1:
                self.pos[0][0] -= 1
                self.pos[0][1] += 1
                self.pos[2][0] += 1
                self.pos[2][1] -= 1
                self.pos[3][0] += 2
                self.pos[3][1] -= 2
                self.orientation = 4
            elif self.orientation == 2:
                self.pos[0][0] += 1
                self.pos[0][1] -= 2
                self.pos[1][1] -= 1
                self.pos[2][0] -= 1
                self.pos[3][0] -= 2
                self.pos[3][1] += 1
                self.orientation = 1
            elif self.orientation == 3:
                self.pos[0][0] -= 2
                self.pos[0][1] += 2
                self.pos[1][0] -= 1
                self.pos[1][1] += 1
                self.pos[3][0] += 1
                self.pos[3][1] -= 1
                self.orientation = 2
            else:
                self.pos[0][0] += 2
                self.pos[0][1] -= 1
                self.pos[1][0] += 1
                self.pos[2][1] += 1
                self.pos[3][0] -= 1
                self.pos[3][1] += 2
                self.orientation = 3
        for i in self.pos:
            board[i[0]][i[1]] = 7

    def update(self):
        if self.orientation in [1, 3]:
            self.bottoms = [0, 1, 2, 3]
            self.lefts = [0]
            self.rights = [3]
        else:
            self.bottoms == [3]
            self.lefts = [0, 1, 2, 3]
            self.rights = [0, 1, 2, 3]

def grid(a, b):
    for m in range(a):
        pygame.draw.line(scrn, white, (0, m * height / a), (width, m * height / a))
    for m in range(b):
        pygame.draw.line(scrn, white, (m * width / b, 0), (m * width / b, height))

def show():
    for i in range(blank_rows):
        for j in range(cols):
            pygame.draw.rect(scrn, grey, pygame.Rect(j * width / cols, i * height / rows, width / cols, height / rows))

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 1:
                pygame.draw.rect(scrn, red, pygame.Rect(j * width / cols, i * height / rows, width / cols, height / rows))
            elif board[i][j] == 2:
                pygame.draw.rect(scrn, green, pygame.Rect(j * width / cols, i * height / rows, width / cols, height / rows))
            elif board[i][j] == 3:
                pygame.draw.rect(scrn, blue, pygame.Rect(j * width / cols, i * height / rows, width / cols, height / rows))
            elif board[i][j] == 4:
                pygame.draw.rect(scrn, orange, pygame.Rect(j * width / cols, i * height / rows, width / cols, height / rows))
            elif board[i][j] == 5:
                pygame.draw.rect(scrn, yellow, pygame.Rect(j * width / cols, i * height / rows, width / cols, height / rows))
            elif board[i][j] == 6:
                pygame.draw.rect(scrn, magenta, pygame.Rect(j * width / cols, i * height / rows, width / cols, height / rows))
            elif board[i][j] == 7:
                pygame.draw.rect(scrn, cyan, pygame.Rect(j * width / cols, i * height / rows, width / cols, height / rows))

    grid(rows, cols)

def freeBelow():
    freeBelow_var = True
    for i in temp_block.bottoms:
        if freeBelow_var:
            temp = temp_block.pos[i].copy()
            # print(board[temp[0] + 1][temp[1]])
            try:
                freeBelow_var = freeBelow_var and not(board[temp[0] + 1][temp[1]])
            except:
                return False
        else:
            return False
    return freeBelow_var

def freeLeft():
    freeLeft_var = True
    for i in temp_block.lefts:
        if freeLeft_var:
            temp = temp_block.pos[i]
            if temp[1]:
                freeLeft_var = freeLeft_var and not(board[temp[0]][temp[1] - 1])
            else:
                return False
        else:
            return False
    return freeLeft_var

def freeRight():
    freeRight_var = True
    for i in temp_block.rights:
        if freeRight_var:
            temp = temp_block.pos[i]
            try:
                freeRight_var = freeRight_var and not(board[temp[0]][temp[1] + 1])
            except:
                return False
        else:
            return False
    return freeRight_var

def newBlock():
    newBlock_var = random.randint(1, 7)
    if newBlock_var == 1:
        return BlockZ()
    elif newBlock_var == 2:
        return BlockS()
    elif newBlock_var == 3:
        return BlockJ()
    elif newBlock_var == 4:
        return BlockL()
    elif newBlock_var == 5:
        return BlockO()
    elif newBlock_var == 6:
        return BlockT()
    else:
        return BlockI()

def update():
    global temp_block

    if freeBelow():
        for i in range(len(temp_block.pos) - 1, -1, -1):
            temp = temp_block.pos[i].copy()
            board[temp[0]][temp[1]] = 0
            board[temp[0] + 1][temp[1]] = temp_block.kind
            temp_block.pos[i][0] += 1
    else:
        temp_block = newBlock()

def translateBlock(way):
    global temp_block

    if way == "left":
        if freeLeft():
            for i in range(len(temp_block.pos)):
                temp = temp_block.pos[i].copy()
                board[temp[0]][temp[1]] = 0
                board[temp[0]][temp[1] - 1] = temp_block.kind
                temp_block.pos[i][1] -= 1
    else:
        if freeRight():
            for i in range(len(temp_block.pos)):
                temp = temp_block.pos[i].copy()
                board[temp[0]][temp[1]] = 0
                board[temp[0]][temp[1] + 1] = temp_block.kind
                temp_block.pos[i][1] += 1

temp_block = newBlock()

while running:
    scrn.fill(black)

    t += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == "q":
                temp_block.rotate("acw")
            if pygame.key.name(event.key) == "e":
                temp_block.rotate("cw")
            if pygame.key.name(event.key) == "left":
                translateBlock("left")
            if pygame.key.name(event.key) == "right":
                translateBlock("right")

    temp_block.update()
    print(temp_block.bottoms)

    if not(t % 1):
        update()
        t = 0

    show()

    pygame.display.update()
    time.sleep(0.5)

pygame.quit()