import math, pygame, random, time
import import_vectors as vect

pygame.init()

width = 300
height = 600
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
running = True
cor = 1
damping = 0.0001

scrn = pygame.display.set_mode((width, height))

class Puck:
    def __init__(self):
        self.radius = 10
        self.pos = vect.Vector(width / 2, 7 * height / 12)
        self.vel = vect.Vector(0, 0)
        self.score = False

    def show(self):
        pygame.draw.circle(scrn, red, (self.pos.x, self.pos.y), self.radius)

    def update(self):
        try:
            self.vel = self.vel.mult(1 - damping)
        except:
            pass
        self.pos = vect.add(self.pos, self.vel)

        if self.pos.y < -self.radius or self.pos.y > height + self.radius:
            self.pos = vect.Vector(width / 2, 7 * height / 12)
            self.vel = vect.Vector(0, 0)
            self.score = False

    def checkEdges(self):
        if self.pos.x <= self.radius or self.pos.x >= width - self.radius:
            self.vel.x *= -1
        if not(self.score):
            if self.pos.y <= self.radius or self.pos.y >= height - self.radius:
                if self.pos.x < width / 3 + self.radius or self.pos.x > 2 * width / 3 - self.radius:
                    self.vel.y *= -1
                else:
                    self.score = True

class Player:
    def __init__(self, px, py):
        self.radius = 20
        self.prev_pos = vect.Vector(px, py)
        self.pos = self.prev_pos
        self.vel = vect.sub(self.pos, self.prev_pos)

    def show(self):
        pygame.draw.circle(scrn, black, (self.pos.x, self.pos.y), self.radius)

def collision(a, b):
    disp = vect.sub(b.pos, a.pos)
    if (disp.mag() <= (a.radius + b.radius)):
        while (disp.mag() <= (a.radius + b.radius)):
            b.pos = vect.add(b.pos, disp.mult(0.01))
            disp = vect.sub(b.pos, a.pos)
        parallelCompA = disp.setMag(vect.dot(disp.normalise(), a.vel))
        parallelCompB = disp.setMag(vect.dot(disp.normalise(), b.vel))
        perpCompB = vect.sub(b.vel, parallelCompB)
        v2 = vect.sub(parallelCompA.mult(cor + 1), parallelCompB.mult(cor))
        b.vel = vect.add(perpCompB, v2)

p1 = Player(width / 2, 5 * height / 6)
puck = Puck()

while running:
    scrn.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    p1.prev_pos = p1.pos
    p1.pos = vect.Vector(sorted([p1.radius, pygame.mouse.get_pos()[0], width - p1.radius])[1], max(height / 2, pygame.mouse.get_pos()[1]))
    p1.vel = vect.sub(p1.pos, p1.prev_pos).mult(0.01)
    collision(p1, puck)
    puck.checkEdges()
    puck.update()

    pygame.draw.line(scrn, green, (0, height / 2), (width, height / 2), 2)
    pygame.draw.line(scrn, blue, (width / 3, 0), (2 * width / 3, 0), 2)
    pygame.draw.line(scrn, blue, (width / 3, height - 2), (2 * width / 3, height - 2), 2)
    pygame.draw.circle(scrn, green, (width / 2, height / 2), 50, 2)
    pygame.draw.circle(scrn, green, (width / 2, height / 2), 5)
    p1.show()
    puck.show()
    # if p1.vel.mag() != 0:
    #     print(p1.vel.mag())

    pygame.display.update()

pygame.quit()