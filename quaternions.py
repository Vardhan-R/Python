import math, pygame, random

pygame.init()

width = 600
height = 600
black = (0, 0, 0)
running = False

scrn = pygame.display.set_mode((width, height))

class Quaternion:
    def __init__(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z
        self.q = str(w) + " + " + str(x) + "i + " + str(y) + "j + " + str(z) + "k"

    def mag(self): return math.sqrt(self.w ** 2 + self.x ** 2 + self.y ** 2 + self.z ** 2)

    def magSq(self): return self.w ** 2 + self.x ** 2 + self.y ** 2 + self.z ** 2

def add(*qs):
    w = 0
    x = 0
    y = 0
    z = 0
    for q in qs:
        w += q.w
        x += q.x
        y += q.y
        z += q.z
    return Quaternion(w, x, y, z)

def sub(q1, q2): return Quaternion(q1.w - q2.w, q1.x - q2.x, q1.y - q2.y, q1.z - q2.z)

def scalarMult(s, q): return Quaternion(s * q.w, s * q.x, s * q.y, s * q.z)

def mult(q1, q2): return Quaternion(q1.w * q2.w - q1.x * q2.x - q1.y * q2.y - q1.z * q2.z, q1.w * q2.x + q1.x * q2.w + q1.y * q2.z - q1.z * q2.y, q1.w * q2.y + q1.y * q2.w - q1.x * q2.z + q1.z * q2.x, q1.w * q2.z + q1.z * q2.w + q1.x * q2.y - q1.y * q2.x)

while running:
    scrn.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    pygame.display.update()

pygame.quit()