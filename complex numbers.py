import math, pygame, random
pygame.init()
width = 600
height = 600
xl = -5
xr = 5
yd = -5
yu = 5
black = (0, 0, 0)
dark_grey = (85, 85, 85)
light_grey = (170, 170, 170)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
violet = (255, 0, 255)
all_colours = [red, green, blue, yellow, violet]
running = True
scrn = pygame.display.set_mode((width, height))
font_size = 16
font = pygame.font.Font("freesansbold.ttf", font_size)

def grid(xl, xr, yd, yu): # xl as in x-left, xr as in x-right, yd as in y-down and yu as in y-up
    for i in range(xl, xr + 1):
        pygame.draw.line(scrn, dark_grey, ((i - xl) * width / (xr - xl), 0), ((i - xl) * width / (xr - xl), height))
        if i:
            text = font.render(str(i), True, white)
            scrn.blit(text, ((i - xl) * width / (xr - xl) - 6, yu * height / (yu - yd) + 2))
    for i in range(yd, yu + 1):
        pygame.draw.line(scrn, dark_grey, (0, (yu - i) * height / (yu - yd)), (width, (yu - i) * height / (yu - yd)))
        if yu + yd - i:
            text = font.render(str(yu + yd - i), True, white)
            scrn.blit(text, (width * xl / (xl - xr) - 14, height * (i - yd) / (yu - yd) - 6))
    pygame.draw.line(scrn, light_grey, (width * xl / (xl - xr), 0), (width * xl / (xl - xr), height), 2)
    pygame.draw.line(scrn, light_grey, (0, height * yu / (yu - yd)), (width, height * yu / (yu - yd)), 2)
    text = font.render("0", True, white)
    scrn.blit(text, (width * xl / (xl - xr) - 10, height * yu / (yu - yd) + 2))

def write(re, im): return str(re) + " + " + str(im) + "i"

class Comp:
    def __init__(self, r, i):
        self.r = r
        self.i = i
        self.z = str(r) + " + " + str(i) + "i"

    def copy(self): return Comp(self.r, self.i)

    def mag(self): return math.sqrt(self.r ** 2 + self.i ** 2)

    def magSq(self): return self.r ** 2 + self.i ** 2

    def normalise(self): return self.write(self.r / self.mag(), self.i / self.mag())

    def setMag(self, m):
        try: return self.write(m * self.r / self.mag(), m * self.i / self.mag())
        except: pass

    def angle(self):
        if math.atan2(self.i, self.r) < 0: return 2 * math.pi + math.atan2(self.i, self.r)
        else: return math.atan2(self.i, self.r)

    def plot(self, clr):
        pygame.draw.circle(scrn, clr, (width * (xl - self.r) / (xl - xr), height * (yu - self.i) / (yu - yd)), 4)

def add(z1, z2): return Comp(z1.r + z2.r, z1.i + z2.i)
def sub(z1, z2): return Comp(z1.r - z2.r, z1.i - z2.i)
def mult(z1, z2): return Comp(z1.r * z2.r - z1.i * z2.i, z1.r * z2.i + z1.i * z2.r)
def root(n, z):
    roots = []
    for k in range(n): roots.append(Comp((z.mag() ** (1 / n)) * math.cos((z.angle() + 2 * math.pi * k) / n), (z.mag() ** (1 / n)) * math.sin((z.angle() + 2 * math.pi * k) / n)))
    return roots
def compPolar(r, t):
    return Comp(r * math.cos(t), r * math.sin(t))
def compExp(r, t):
    return Comp(r * math.cos(t), r * math.sin(t))

z1 = Comp(3, 4)
z2 = Comp(5, 12)
z3 = mult(z1, z2)
# print(z3.z)
z4 = z1.copy()
z4.r = 5
# print(z1.r, z1.i, z4.r, z4.i)

l = [Comp(1, 0), Comp(3, 2), Comp(0, 1), Comp(-2, 1), Comp(-2, 0), Comp(-3, -4), Comp(0, -3), Comp(4, -5)]
for i in l: print(i.z)
rts = root(3, Comp(1, 2))

while running:
    scrn.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
    grid(xl, xr, yd, yu)
    for i in rts: i.plot(red)
    # l[0].plot(red)
    # l[1].plot(green)
    # l[2].plot(blue)
    # l[3].plot(yellow)
    # l[4].plot(violet)
    # l[5].plot(dark_grey)
    # l[6].plot(light_grey)
    # l[7].plot(white)
    pygame.display.update()
pygame.quit()

# root
# exp form
# polar form
# plot on graph