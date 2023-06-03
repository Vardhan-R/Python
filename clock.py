import pygame, manim, math, time

pygame.init()

width = 800
height = 800
half_canvas = (width / 2, height / 2)
pi_by_2 = math.pi / 2
pi_by_6 = math.pi / 6
pi_by_30 = math.pi / 30
pi_by_360 = math.pi / 360
pi_by_1800 = math.pi / 1800
pi_by_21600 = math.pi / 21600
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

hr_hand = Vector(0, half_canvas[0] - 200)
min_hand = Vector(0, half_canvas[0] - 120)
sec_hand = Vector(0, half_canvas[0] - 85)

scrn.fill(manim.BLACK)

pygame.draw.circle(scrn, manim.WHITE, (half_canvas[0], half_canvas[1]), half_canvas[0] - 25, 1)

for i in range(12):
    text = font.render(str(i + 1), True, manim.WHITE)
    ang = (i + 1) * pi_by_6 - pi_by_2
    if i < 10:
        scrn.blit(text, (half_canvas[0] + (half_canvas[0] - 60) * math.cos(ang) - 7, half_canvas[1] + (half_canvas[0] - 60) * math.sin(ang) - 12))
    else:
        scrn.blit(text, (half_canvas[0] + (half_canvas[0] - 60) * math.cos(ang) - 14, half_canvas[1] + (half_canvas[0] - 60) * math.sin(ang) - 12))

for i in range(60):
    ang = i * pi_by_30 - pi_by_2
    if i % 5:
        pygame.draw.line(scrn, manim.WHITE, (half_canvas[0] + (half_canvas[0] - 25) * math.cos(ang), half_canvas[1] + (half_canvas[0] - 25) * math.sin(ang)), (half_canvas[0] + (half_canvas[0] - 35) * math.cos(ang), half_canvas[1] + (half_canvas[0] - 35) * math.sin(ang)))
    else:
        pygame.draw.line(scrn, manim.WHITE, (half_canvas[0] + (half_canvas[0] - 25) * math.cos(ang), half_canvas[1] + (half_canvas[0] - 25) * math.sin(ang)), (half_canvas[0] + (half_canvas[0] - 50) * math.cos(ang), half_canvas[1] + (half_canvas[0] - 50) * math.sin(ang)))

font = pygame.font.SysFont("Courier New", 60)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    h = time.strftime("%H", time.localtime())
    m = time.strftime("%M", time.localtime())
    s = time.strftime("%S", time.localtime())

    text = font.render(f"{h}:{m}:{s}", True, manim.WHITE)

    h = int(h)
    m = int(m)
    s = int(s)

    pygame.draw.circle(scrn, manim.BLACK, (half_canvas[0], half_canvas[1]), half_canvas[0] - 80)

    hr_hand = hr_hand.setDir(h * pi_by_6 + m * pi_by_360 + s * pi_by_21600 - pi_by_2)
    min_hand = min_hand.setDir(m * pi_by_30 + s * pi_by_1800 - pi_by_2)
    sec_hand = sec_hand.setDir(s * pi_by_30 - pi_by_2)

    pygame.draw.line(scrn, manim.BLUE, (half_canvas[0], half_canvas[1]), (half_canvas[0] + hr_hand.x, half_canvas[1] + hr_hand.y))
    pygame.draw.line(scrn, manim.GREEN, (half_canvas[0], half_canvas[1]), (half_canvas[0] + min_hand.x, half_canvas[1] + min_hand.y))
    pygame.draw.line(scrn, manim.RED, (half_canvas[0], half_canvas[1]), (half_canvas[0] + sec_hand.x, half_canvas[1] + sec_hand.y))

    scrn.blit(text, (half_canvas[0], half_canvas[1]))

    pygame.display.update()
    time.sleep(0.5)

pygame.quit()
