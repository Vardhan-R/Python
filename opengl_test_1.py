from built_modules import import_matrices as mat, import_vectors as vect
from manim import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math, pygame

pygame.init()

width = 800
height = 600
canvas = (width, height)
running = True
clrs = [(1, 0, 0), (0, 0, 1), (1, 0.5, 0), (0, 1, 0), (1, 1, 0), (1, 1, 1)]
prev_key_states = {"w": False, "s": False, "a": False, "d": False}
phi = 0
theta = 0
n = 0
n_max = 1000
dt = 90 / n_max
t = 0

pygame.display.set_mode(canvas, pygame.DOUBLEBUF | pygame.OPENGL)

class Cuboid:
    def __init__(self, centre: tuple = (0, 0, 0), a: float | int = 2, b: float | int = 2, c: float | int = 2):
        self.half_a = a / 2
        self.half_b = b / 2
        self.half_c = c / 2
        self.vertices = (
            ([centre[0] + self.half_a], [centre[1] + self.half_b], [centre[2] + self.half_c]),
            ([centre[0] - self.half_a], [centre[1] + self.half_b], [centre[2] + self.half_c]),
            ([centre[0] - self.half_a], [centre[1] - self.half_b], [centre[2] + self.half_c]),
            ([centre[0] + self.half_a], [centre[1] - self.half_b], [centre[2] + self.half_c]),
            ([centre[0] + self.half_a], [centre[1] + self.half_b], [centre[2] - self.half_c]),
            ([centre[0] - self.half_a], [centre[1] + self.half_b], [centre[2] - self.half_c]),
            ([centre[0] - self.half_a], [centre[1] - self.half_b], [centre[2] - self.half_c]),
            ([centre[0] + self.half_a], [centre[1] - self.half_b], [centre[2] - self.half_c])
        )
        self.current_vertices = self.vertices

        self.edges = []
        for i in range(4):
            self.edges.append((i % 4, (i + 1) % 4))
            self.edges.append((i % 4 + 4, (i + 1) % 4 + 4))
            self.edges.append((i, i + 4))
        self.edges = tuple(self.edges)

        self.faces = (
            (0, 1, 2, 3),
            (1, 5, 7, 2),
            (5, 4, 7, 6),
            (4, 0, 3, 7),
            (4, 5, 1, 0),
            (3, 2, 6, 7)
        )

    # def __init__(self, vertices: tuple = ((1, 1, 1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, -1))):
    #     self.vertices = vertices

    def rotate(self, a: float | int, axis: str):
        if axis == "x":
            m = [[1, 0, 0],
                 [0, math.cos(a), math.sin(a)],
                 [0, -math.sin(a), math.cos(a)]]
        elif axis == "y":
            m = [[math.cos(a), 0, math.sin(a)],
                 [0, 1, 0],
                 [-math.sin(a), 0, math.cos(a)]]
        else: # axis == "z"
            m = [[math.cos(a), math.sin(a), 0],
                 [-math.sin(a), math.cos(a), 0],
                 [0, 0, 1]]
        self.current_vertices = [mat.mult(m, x) for x in self.current_vertices]

    def show(self):
        # glBegin(GL_QUADS)
        # i = 0
        # for face in self.faces:
        #     glColor3fv(clrs[i])
        #     i += 1
        #     for vertex in face:
        #         glVertex3fv(self.vertices[vertex])
        # glEnd()

        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                temp = self.current_vertices[vertex]
                glVertex3fv([x[0] for x in temp])
        glEnd()

    def generateEdges(self):
        pass

    def generateFaces(self):
        pass

gluPerspective(45, width / height, 0.1, 50)

glTranslatef(0, 0, -8)

# cuboid_1 = Cuboid()
cuboid_1 = Cuboid(a = 3, b = 2, c = 1)
# cuboid_1.generateEdges()
# cuboid_2 = Cuboid()
cuboid_2 = Cuboid(a = 3, b = 2, c = 1)

a = [[0.19715, -0.80329, 0.56201],
     [-0.80241, 0.19715, 0.56327],
     [-0.56327, -0.56201, -0.6057]]

cuboid_2.current_vertices = [mat.mult(a, i) for i in cuboid_2.current_vertices]
# cuboid_2.current_vertices = [([v[0][0] + math.pi * v[2][0] / 2], [v[1][0] + math.pi * v[2][0] / 2], [v[2][0] - math.pi * (v[0][0] + v[1][0]) / 2]) for v in cuboid_2.current_vertices]

while running:
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            current_key = pygame.key.name(event.key)
            if current_key == "w":
                # glRotatef(1, -1, 0, 0)
                cuboid_1.rotate(dt * DEGREES, "x")
                theta += DEGREES
            elif current_key == "s":
                # glRotatef(1, 1, 0, 0)
                cuboid_1.rotate(-dt * DEGREES, "x")
                theta -= DEGREES
            elif current_key == "a":
                # glRotatef(1, 0, 1, 0)
                cuboid_1.rotate(-dt * DEGREES, "y")
                phi -= DEGREES
            elif current_key == "d":
                # glRotatef(1, 0, -1, 0)
                cuboid_1.rotate(dt * DEGREES, "y")
                phi += DEGREES
            prev_key_states[current_key] = True

        if event.type == pygame.KEYUP:
            prev_key_states[current_key] = False
            # print(math.cos(phi * DEGREES) - math.sin(phi * DEGREES))

    # if prev_key_states["w"]:
    #     # glRotatef(1, -1, 0, 0)
    #     cuboid_1.rotate(DEGREES, "x")
    #     theta += DEGREES
    # if prev_key_states["s"]:
    #     # glRotatef(1, 1, 0, 0)
    #     cuboid_1.rotate(-DEGREES, "x")
    #     theta -= DEGREES
    # if prev_key_states["a"]:
    #     # glRotatef(1, 0, 1, 0)
    #     cuboid_1.rotate(-DEGREES, "y")
    #     phi -= DEGREES
    # if prev_key_states["d"]:
    #     # glRotatef(1, 0, -1, 0)
    #     cuboid_1.rotate(DEGREES, "y")
    #     phi += DEGREES

    glColor3fv((0, 1, 0))
    cuboid_1.show()
    glColor3fv((0, 0, 1))
    cuboid_2.show()

    # print(glRotate)

    # glRotatef(1, 1, 1, 1)
    if not(t % 1) and n < n_max:
        if t % 2:
            cuboid_1.rotate(dt * DEGREES, "y")
            n += 1
        else:
            cuboid_1.rotate(dt * DEGREES, "x")
    t += 1

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
