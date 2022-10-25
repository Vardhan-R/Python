from built_modules import import_vectors as vect
from OpenGL.GL import *
from OpenGL.GLU import *
import math, numpy as np, pygame, random, time

pygame.init()

width = 1600
height = 1200
p = []
for i in range(3):
    p.append((random.randrange(-250, 250) / 100, random.randrange(-250, 250) / 100, random.randrange(-250, 250) / 100))
# p = [(-2, 1, 0), (-1.5, 0, -1), (-1, -1, 0), (-0.5, 0, 1), (0, 1, 0), (0.5, 0, -1), (1, -1, 0), (1.5, 0, 1), (2, 1, 0)]
# temp_lst_1 = [math.pi * x / 5 for x in range(10)] # helix
# temp_lst_2 = [(math.cos(x), math.sin(x)) for x in temp_lst_1]
# p = list(np.reshape(np.array([[(temp_lst_2[y][0], temp_lst_2[y][1], x + y / 10) for y in range(10)] for x in range(-5, 5)]), (1, -1, 3))[0])

# t < 2 * math.pi * (nN - 2) / (nN - 1) ==> non-cyclic

pts = []
all_pts = []
nN = len(p)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
running = True
pmb1s = False

class Circle:
    def __init__(self, colour: tuple, radius: float | int = 1, points: int = 32):
        self.clr = colour
        #, centre: vect.Vector = vect.Vector(0, 0, 0)
        # self.centre = centre
        self.radius = radius
        self.pts_arr = np.array([(radius * math.cos(2 * math.pi * x / points), radius * math.sin(2 * math.pi * x / points), 0) for x in range(points)])

    def rotate(self, theta: float | int = 0, phi: float | int = 0):
        r_x = np.array([[1, 0, 0],
                        [0, math.cos(theta), -math.sin(theta)],
                        [0, math.sin(theta), math.cos(theta)]])
        r_y = np.array([[math.cos(phi), 0, -math.sin(phi)],
                        [0, 1, 0],
                        [math.sin(phi), 0, math.cos(phi)]])
        r_yx = np.matmul(r_y, r_x)
        self.pts_arr = np.array([np.matmul(r_yx, i) for i in self.pts_arr])

    def show(self, centre):
        glColor3fv(self.clr)
        glBegin(GL_LINE_LOOP)
        for i in self.pts_arr:
            glVertex3fv(tuple(centre + i))
        glEnd()

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
        try:
            old_mag = self.mag()
            self.r = m * self.r / old_mag
            self.i = m * self.i / old_mag
        except: pass

    def angle(self):
        if math.atan2(self.i, self.r) < 0: return 2 * math.pi + math.atan2(self.i, self.r)
        else: return math.atan2(self.i, self.r)

    # def plot(self, clr):
    #     pygame.draw.circle(scrn, clr, (width * (xl - self.r) / (xl - xr), height * (yu - self.i) / (yu - yd)), 4)

scrn = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.OPENGL)

def write(re, im): return str(re) + " + " + str(im) + "i"
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

def sortCheck(l):
    for m in range(len(l) - 1):
        if l[m] < l[m + 1]:
            return False
    return True

def generateEpicycles(p):
    pts = []
    freqs = []
    coeffs = []
    coeffs_mag = []

    for i in p:
        pts.append(Comp(i[0], i[1]))

    for i in range(round(-(nN - 1) / 2), round((nN + 1) / 2)):
        freqs.append(i)

    for i in freqs:
        c = Comp(0, 0)
        for j in range(nN):
            c = add(c, mult(pts[j], Comp(math.cos(2 * math.pi * i * j / nN), -math.sin(2 * math.pi * i * j / nN))))
        coeffs.append(c)

    for i in coeffs:
        coeffs_mag.append(i.mag())

    while not(sortCheck(coeffs_mag)):
        for i in range(len(coeffs_mag) - 1):
            if coeffs_mag[i] < coeffs_mag[i + 1]:
                temp = coeffs_mag[i]
                coeffs_mag[i] = coeffs_mag[i + 1]
                coeffs_mag[i + 1] = temp

                temp = coeffs[i]
                coeffs[i] = coeffs[i + 1]
                coeffs[i + 1] = temp

                temp = freqs[i]
                freqs[i] = freqs[i + 1]
                freqs[i + 1] = temp

    return (freqs, coeffs, coeffs_mag)

def calculatePoint(t, freqs, coeffs, coeffs_mag = None, plane = "xy", initial = None):
    circle_centres = []
    circle_radii = []
    lines = [(0, 0, 0)]
    pt = Comp(0, 0)
    if plane == "xy":
        for i in range(len(freqs)):
            temp_pt = mult(coeffs[i], compExp(1, freqs[i] * t))
            circle_radii.append(coeffs_mag[i] / nN)
            temp_comp = add(pt, temp_pt)
            circle_centres.append((pt.r / nN, pt.i / nN, 0))
            lines.append((temp_comp.r / nN, temp_comp.i / nN, 0))
        pt = add(pt, temp_pt)
        pt.setMag(pt.mag() / nN)
        pt = np.array([pt.r, pt.i, 0])
        # pygame.draw.circle(scrn, white, (p[i][0], p[i][1]), 2)
        # pygame.draw.circle(scrn, green, (pt.r / nN, pt.i / nN), coeffs_mag[i] / nN, width = 1)
        # pygame.draw.line(scrn, green, (pt.r / nN, pt.i / nN), (add(pt, temp_pt).r / nN, add(pt, temp_pt).i / nN))
    elif plane == "xz":
        for i in range(len(freqs)):
            temp_pt = mult(coeffs[i], compExp(1, freqs[i] * t))
            circle_radii.append(coeffs_mag[i] / nN)
            temp_comp = add(pt, temp_pt)
            circle_centres.append((pt.r / nN, 0, pt.i / nN))
            lines.append((temp_comp.r / nN, 0, temp_comp.i / nN))
        pt = add(pt, temp_pt)
        pt.setMag(pt.mag() / nN)
        pt = np.array([pt.r, 0, pt.i])
    else: # plane == "yz"
        for i in range(len(freqs)):
            temp_pt = mult(coeffs[i], compExp(1, freqs[i] * t))
            circle_radii.append(coeffs_mag[i] / nN)
            temp_comp = add(pt, temp_pt)
            circle_centres.append((0, pt.r / nN, pt.i / nN))
            lines.append((0, temp_comp.r / nN, temp_comp.i / nN))
        pt = add(pt, temp_pt)
        pt.setMag(pt.mag() / nN)
        pt = np.array([0, pt.r, pt.i])
    # pygame.draw.circle(scrn, red, (pt.r, pt.i), 2)
    circle_centres = np.array(circle_centres)
    lines = np.array(lines)
    if type(initial) == np.ndarray:
        circle_centres += initial
        lines += initial
    return (pt, circle_centres, circle_radii, lines)

p_xy = [i[:2] for i in p]
p_xz = [(i[0], i[2]) for i in p]
p_yz = [i[1:] for i in p]

freqs_xy, coeffs_xy, coeffs_mag_xy = generateEpicycles(p_xy)
freqs_xz, coeffs_xz, coeffs_mag_xz = generateEpicycles(p_xz)
freqs_yz, coeffs_yz, coeffs_mag_yz = generateEpicycles(p_yz)

t = 0

gluPerspective(45, width / height, 0.1, 50)

glTranslatef(0, 0, -10)

glPointSize(5)

# theta ==> xz; phi ==> yz

while running:
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_pressed()[0]:
        if pmb1s:
            current_mouse_pos = pygame.mouse.get_pos()
            glRotatef(1, current_mouse_pos[1] - initial_mouse_pos[1], current_mouse_pos[0] - initial_mouse_pos[0], 0)
            initial_mouse_pos = current_mouse_pos
        else:
            pmb1s = True
            initial_mouse_pos = pygame.mouse.get_pos()
    else:
        pmb1s = False

    # if t < 2 * math.pi * (nN - 2) / (nN - 1):
    if t < 2 * math.pi:
        pt_xy, circle_centres_xy, circle_radii_xy, lines_xy = calculatePoint(t, freqs_xy, coeffs_xy, coeffs_mag_xy, "xy")
        circles_xy = [Circle((0, 1, 0), circle_radii_xy[i]) for i in range(nN)]
        # circle_centres_xy = np.array([[i[0], i[1], 0] for i in circle_centres_xy])
        # lines_xy = np.array([[i[0], i[1], 0] for i in lines_xy])
        pt_xz, circle_centres_xz, circle_radii_xz, lines_xz = calculatePoint(t, freqs_xz, coeffs_xz, coeffs_mag_xz, "xz", lines_xy[-1])
        circles_xz = [Circle((0, 1, 0), circle_radii_xz[i]) for i in range(nN)]
        # circle_centres_xz = np.array([[i[0], 0, i[1]] for i in circle_centres_xz])
        # lines_xz = np.array([[i[0], 0, i[1]] for i in lines_xz])
        pt_yz, circle_centres_yz, circle_radii_yz, lines_yz = calculatePoint(t, freqs_yz, coeffs_yz, coeffs_mag_yz, "yz", lines_xz[-1])
        circles_yz = [Circle((0, 1, 0), circle_radii_yz[i]) for i in range(nN)]
        # circle_centres_yz = np.array([[0, i[0], i[1]] for i in circle_centres_yz])
        # lines_yz = np.array([[0, i[0], i[1]] for i in lines_yz])
        # lines_xz[0] += lines_xy[-1]
        # lines_yz[0] += lines_xz[-1]
        # print(lines_xy[-1])
        for i in range(nN):
            # circle_centres_yz[i] += lines_xz[-1] + lines_xy[-1]
            # lines_yz[i + 1] += lines_xz[-1] + lines_xy[-1]
            # circle_centres_xz[i] += lines_xy[-1]
            # lines_xz[i + 1] += lines_xy[-1]
            circles_xz[i].rotate(math.pi / 2)
            circles_yz[i].rotate(0, math.pi / 2)
            circles_xy[i].show(circle_centres_xy[i])
            circles_xz[i].show(circle_centres_xz[i])
            circles_yz[i].show(circle_centres_yz[i])
        pt = tuple((pt_xy + pt_xz + pt_yz) / 2)
        all_pts.append(pt)
        t += math.pi / 5000

        # xy
        glBegin(GL_LINES)
        for i in lines_xy:
            glVertex3fv((i[0], i[1], 0))
        glEnd()
        glBegin(GL_LINES)
        for i in lines_xy[1:]:
            glVertex3fv((i[0], i[1], 0))
        glEnd()
        # xz
        glBegin(GL_LINES)
        for i in lines_xz:
            glVertex3fv((i[0], 0, i[1]))
        glEnd()
        glBegin(GL_LINES)
        for i in lines_xz[1:]:
            glVertex3fv((i[0], 0, i[1]))
        glEnd()
        # yz
        glBegin(GL_LINES)
        for i in lines_yz:
            glVertex3fv((0, i[0], i[1]))
        glEnd()
        glBegin(GL_LINES)
        for i in lines_yz[1:]:
            glVertex3fv((0, i[0], i[1]))
        glEnd()

        glBegin(GL_POINTS)
        glColor3fv((1, 1, 1))
        glVertex3fv(pt)
        glEnd()

        glBegin(GL_POINTS)
        glColor3fv((1, 0, 0))
        for i in p:
            glVertex3fv(i)
        glEnd()
    else:
        glBegin(GL_LINES)
        glColor3fv((1, 1, 1))
        for i in all_pts:
            glVertex3fv(i)
        glEnd()

        glBegin(GL_POINTS)
        glColor3fv((1, 0, 0))
        for i in p:
            glVertex3fv(i)
        glEnd()

    pygame.display.flip()

# for i in p:
#     pygame.draw.circle(scrn, white, (i[0], i[1]), 2)
# glBegin(GL_LINES)
# glColor3fv((1, 1, 1))
# for i in all_pts:
#     glVertex3fv(i)
# glEnd()

# glBegin(GL_POINTS)
# glColor3fv((1, 0, 0))
# for i in p:
#     glVertex3fv(i)
# glEnd()

# pygame.display.flip()

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

pygame.quit()