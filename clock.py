import pygame, math, time

pygame.init()

width = 200
height = 200
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
running = True
font = pygame.font.SysFont("Courier New", 24)

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

# hr_hand = Vector(0, 200)
# min_hand = Vector(0, 240)
# sec_hand = Vector(0, 270)
hr_hand = Vector(0, width / 2 - 40)
min_hand = Vector(0, width / 2 - 35)
sec_hand = Vector(0, width / 2 - 30)

while running:
    scrn.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    h = int(time.strftime("%H", time.localtime()))
    m = int(time.strftime("%M", time.localtime()))
    s = int(time.strftime("%S", time.localtime()))

    hr_hand = hr_hand.setDir(h * math.pi / 6 + m * math.pi / 360 + s * math.pi / 21600 - math.pi / 2)
    min_hand = min_hand.setDir(m * math.pi / 30 + s * math.pi / 1800 - math.pi / 2)
    sec_hand = sec_hand.setDir(s * math.pi / 30 - math.pi / 2)

    pygame.draw.circle(scrn, white, (width / 2, height / 2), width / 2 - 25, 1)

    for i in range(12):
        text = font.render(str(i + 1), True, white)
        ang = (i + 1) * math.pi / 6 - math.pi / 2
        if i < 10:
            scrn.blit(text, (width / 2 + (width / 2 - 60) * math.cos(ang) - 7, height / 2 + (width / 2 - 60) * math.sin(ang) - 12))
        else:
            scrn.blit(text, (width / 2 + (width / 2 - 60) * math.cos(ang) - 14, height / 2 + (width / 2 - 60) * math.sin(ang) - 12))

    for i in range(60):
        ang = i * math.pi / 30 - math.pi / 2
        if i % 5:
            pygame.draw.line(scrn, white, (width / 2 + (width / 2 - 25) * math.cos(ang), height / 2 + (width / 2 - 25) * math.sin(ang)), (width / 2 + (width / 2 - 35) * math.cos(ang), height / 2 + (width / 2 - 35) * math.sin(ang)))
        else:
            pygame.draw.line(scrn, white, (width / 2 + (width / 2 - 25) * math.cos(ang), height / 2 + (width / 2 - 25) * math.sin(ang)), (width / 2 + (width / 2 - 50) * math.cos(ang), height / 2 + (width / 2 - 50) * math.sin(ang)))

    pygame.draw.line(scrn, blue, (width / 2, height / 2), (width / 2 + hr_hand.x, height / 2 + hr_hand.y))
    pygame.draw.line(scrn, green, (width / 2, height / 2), (width / 2 + min_hand.x, height / 2 + min_hand.y))
    pygame.draw.line(scrn, red, (width / 2, height / 2), (width / 2 + sec_hand.x, height / 2 + sec_hand.y))

    pygame.display.update()
    time.sleep(0.5)

pygame.quit()