import math, pygame, random, time

pygame.init()

width = 600
height = 600
running = True
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
rows = 20
cols = 20
h_walls = [] # h as in horizontal
v_walls = [] # v as in vertical

scrn = pygame.display.set_mode((width, height))

class Vector:
    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def mult(self, a):
        return Vector(a * self.x, a * self.y, a * self.z)

    def mag(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def magSq(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def normalise(self):
        if self.mag() != 0:
            return self.mult(1 / self.mag())

    def setMag(self, m):
        return Vector(self.x / self.mag(), self.y / self.mag(), self.z / self.mag()).mult(m)

    def dir(self): # z = 0
        return(math.atan2(self.y, self.x))

    def setDir(self, t): # z = 0
        return Vector(self.mag() * math.cos(t), self.mag() * math.sin(t), self.z)

    def rotate(self, t): # z = 0
        return Vector(self.mag() * math.cos(self.dir() + t), self.mag() * math.sin(self.dir() + t), self.z)

def vectorAdd(a, b):
    return Vector(a.x + b.x, a.y + b.y, a.z + b.z)

def vectorSub(a, b):
    return Vector(a.x - b.x, a.y - b.y, a.z - b.z)

def vectorDot(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z

def vectorCross(a, b):
    return Vector(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x)

def vectorDistBetween(a, b):
    return Vector(a.x - b.x, a.y - b.y, a.z - b.z).mag()

def vectorAngBetween(a, b):
    return math.acos(vectorDot(a, b) / (a.mag() * b.mag()))

for i in range(rows + 1):
    temp = []
    for j in range(cols):
        temp.append(True)
    h_walls.append(temp.copy())

for i in range(rows):
    temp = []
    for j in range(cols + 1):
        temp.append(True)
    v_walls.append(temp.copy())

pos = Vector(0, rows - 1)
final_pos = Vector(cols - 1, 0)

while pos.x != final_pos.x or pos.y != final_pos.y:
        if pos.x == 0 and pos.y == 0:
            move = random.choice([Vector(1, 0), Vector(0, 1)])
        elif pos.x == 0 and pos.y == rows - 1:
            move = random.choice([Vector(1, 0), Vector(0, -1)])
        elif pos.x == cols - 1 and pos.y == rows - 1:
            move = random.choice([Vector(-1, 0), Vector(0, -1)])
        elif pos.x == 0:
            move = random.choice([Vector(1, 0), Vector(0, 1), Vector(0, -1)])
        elif pos.x == cols - 1:
            move = random.choice([Vector(-1, 0), Vector(0, 1), Vector(0, -1)])
        elif pos.y == 0:
            move = random.choice([Vector(-1, 0), Vector(1, 0), Vector(0, 1)])
        elif pos.y == rows - 1:
            move = random.choice([Vector(-1, 0), Vector(1, 0), Vector(0, -1)])
        else:
            move = random.choice([Vector(-1, 0), Vector(1, 0), Vector(0, -1), Vector(0, 1)])

        if move.x == 1:
            v_walls[pos.y][pos.x + 1] = False
        elif move.x == -1:
            v_walls[pos.y][pos.x] = False
        elif move.y == 1:
            h_walls[pos.y + 1][pos.x] = False
        else:
            h_walls[pos.y][pos.x] = False
        pos = vectorAdd(pos, move)

while running:
    scrn.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(rows + 1):
        for j in range(cols):
            if h_walls[i][j]:
                pygame.draw.line(scrn, white, (j * width / cols, i * height / rows), ((j + 1) * width / cols, i * height / rows), 4)

    for i in range(rows):
        for j in range(cols + 1):
            if v_walls[i][j]:
                pygame.draw.line(scrn, white, (j * width / cols, i * height / rows), (j * width / cols, (i + 1) * height / rows), 4)

    pygame.display.update()

pygame.quit()