from built_modules import import_vectors as vect
from manim import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math, pygame

pygame.init()

width = 1600
height = 1200
canvas = (width, height)
running = True
clrs = [(1, 0, 0), (0, 0, 1), (1, 0.5, 0), (0, 1, 0), (1, 1, 0), (1, 1, 1)]
prev_key_states = {"w": False, "s": False, "a": False, "d": False}
phi = 0
theta = 0

pygame.display.set_mode(canvas, pygame.DOUBLEBUF | pygame.OPENGL)

class Cube:
    def __init__(self, centre: tuple = (0, 0, 0), side_length: float | int = 2):
        self.half_side_length = side_length / 2
        self.vertices = (
            (centre[0] + self.half_side_length, centre[1] + self.half_side_length, centre[1] + self.half_side_length),
            (centre[0] - self.half_side_length, centre[1] + self.half_side_length, centre[1] + self.half_side_length),
            (centre[0] - self.half_side_length, centre[1] - self.half_side_length, centre[1] + self.half_side_length),
            (centre[0] + self.half_side_length, centre[1] - self.half_side_length, centre[1] + self.half_side_length),
            (centre[0] + self.half_side_length, centre[1] + self.half_side_length, centre[1] - self.half_side_length),
            (centre[0] - self.half_side_length, centre[1] + self.half_side_length, centre[1] - self.half_side_length),
            (centre[0] - self.half_side_length, centre[1] - self.half_side_length, centre[1] - self.half_side_length),
            (centre[0] + self.half_side_length, centre[1] - self.half_side_length, centre[1] - self.half_side_length)
        )

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

    def show(self):
        glBegin(GL_QUADS)
        i = 0
        for face in self.faces:
            glColor3fv(clrs[i])
            i += 1
            for vertex in face:
                glVertex3fv(self.vertices[vertex])
        glEnd()

        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()

    def generateEdges(self):
        pass

    def generateFaces(self):
        pass

gluPerspective(45, width / height, 0.1, 50)

glTranslatef(0, 0, -5)

cube_1 = Cube()
# cube_1.generateEdges()

while running:
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            current_key = pygame.key.name(event.key)
            if current_key == "w":
                glRotatef(1, -1, 0, 0)
                theta -= 1
            elif current_key == "s":
                glRotatef(1, 1, 0, 0)
                theta += 1
            elif current_key == "a":
                glRotatef(1, 0, 1, 0)
                phi -= 1
            elif current_key == "d":
                glRotatef(1, 0, -1, 0)
                phi += 1
            prev_key_states[current_key] = True

        if event.type == pygame.KEYUP:
            prev_key_states[current_key] = False
            print(math.cos(phi * DEGREES) - math.sin(phi * DEGREES))

    if prev_key_states["w"]:
        glRotatef(1, -1, 0, 0)
        theta -= 1
    if prev_key_states["s"]:
        glRotatef(1, 1, 0, 0)
        theta += 1
    if prev_key_states["a"]:
        glRotatef(1, 0, 1, 0)
        phi -= 1
    if prev_key_states["d"]:
        glRotatef(1, 0, -1, 0)
        phi += 1

    cube_1.show()

    # print(glRotate)

    # glRotatef(1, 1, 1, 1)

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()