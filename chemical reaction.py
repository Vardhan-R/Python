import math, pygame, random, time

pygame.init()

width = 800
height = 600
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
running = True
cor = 1
all_circles = []

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

class Circle:
    def __init__(self, r, px, py, vx, vy, clr):
        self.radius = r
        self.pos = Vector(px, py)
        self.vel = Vector(vx, vy)
        self.clr = clr

    def updatePos(self):
        self.pos = vectorAdd(self.pos, self.vel)

    def checkEgdes(self):
        if self.pos.x <= self.radius:
            self.vel.x *= -cor
            self.pos.x = self.radius
        elif self.pos.x >= width - self.radius:
            self.vel.x *= -cor
            self.pos.x = width - self.radius
        if self.pos.y <= self.radius:
            self.vel.y *= -cor
            self.pos.y = self.radius
        elif self.pos.y >= height - self.radius:
            self.vel.y *= -cor
            self.pos.y = height - self.radius

    def show(self):
        pygame.draw.circle(scrn, self.clr, (self.pos.x, self.pos.y), self.radius)

def collision(a, b, v_threshold, n1, n2, rxn):
    global all_circles
    if (vectorSub(b.pos, a.pos).mag() <= a.radius + b.radius):
        dist = vectorSub(b.pos, a.pos)
        parallelCompA = dist.setMag(vectorDot(dist.normalise(), a.vel))
        parallelCompB = dist.setMag(vectorDot(dist.normalise(), b.vel))
        m1 = a.radius ** 2
        m2 = b.radius ** 2
        # print(vectorSub(parallelCompA, parallelCompB).mag())
        if vectorSub(parallelCompA, parallelCompB).mag() < v_threshold:
            perpCompA = vectorSub(a.vel, parallelCompA)
            perpCompB = vectorSub(b.vel, parallelCompB)
            v1 = vectorAdd(parallelCompA.mult(m1 - cor * m2), parallelCompB.mult(m2 * (cor + 1))).mult(1 / (m1 + m2))
            v2 = vectorAdd(parallelCompB.mult(m2 - cor * m1), parallelCompA.mult(m1 * (cor + 1))).mult(1 / (m1 + m2))
            a.vel = vectorAdd(perpCompA, v1)
            b.vel = vectorAdd(perpCompB, v2)
        elif rxn:
            new_pos = vectorAdd(a.pos, dist.setMag(dist.mag() / 2))
            v_com = vectorAdd(a.vel, b.vel)
            v_com.setMag(v_com.mag() / 2)
            return (Circle(math.sqrt(m1 + m2), new_pos.x, new_pos.y, v_com.x, v_com.y, red), n1, n2)

for i in range(20):
    # all_circles.append(Circle(20, random.randrange(50, width - 50), random.randrange(50, height - 50), random.randint(-50, 50) / 100, random.randrange(-50, 50) / 100, blue))
    all_circles.append(Circle(8, random.randrange(50, width - 50), random.randrange(50, height - 50), random.randint(-50, 50) / 100, random.randrange(-50, 50) / 100, blue))

while running:
    scrn.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_reacted = []
    for i in range(len(all_circles)):
        for j in range(i, len(all_circles)):
            if i != j:
                reacted = collision(all_circles[i], all_circles[j], 0.6, i, j, True)
                if type(reacted) == tuple:
                    all_reacted.append(reacted)
    reacted_numbers = []
    for i in all_reacted:
        reacted_numbers.append(i[1])
        reacted_numbers.append(i[2])
    reacted_numbers.sort(reverse=True)
    for i in reacted_numbers:
        all_circles.pop(i)
    for i in all_reacted:
        all_circles.append(i[0])

    for i in all_circles:
        i.updatePos()
        i.checkEgdes()
        i.show()

    pygame.display.update()

pygame.quit()