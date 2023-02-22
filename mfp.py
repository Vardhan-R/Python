from built_modules import import_matrices as mat, import_vectors as vect
from manim import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math, pygame

pygame.init()

width = 800
height = 600
running = True
l = 3
colours = {"red": (1, 0, 0), "green": (0, 1, 0), "blue": (0, 0, 1), "cyan": (0, 1, 1), "magenta": (1, 0, 1), "yellow": (1, 1, 0), "white": (1, 1, 1), "orange": (1, 0.5, 0), "grey": (0.5, 0.5, 0.5)}
prev_key_states = {"w": False, "a": False, "s": False, "d": False, "q": False, "e": False, "space": False}
flipped = False

pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.OPENGL)

gluPerspective(45, width / height, 0.1, 50)

glTranslatef(0, 0, -8)

while running:
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            current_key = pygame.key.name(event.key)
            if current_key == "w":
                glRotatef(1, 1, 0, 0)
            elif current_key == "a":
                glRotatef(1, 0, 1, 0)
            elif current_key == "s":
                glRotatef(1, -1, 0, 0)
            elif current_key == "d":
                glRotatef(1, 0, -1, 0)
            elif current_key == "q":
                glRotatef(1, 0, 0, -1)
            elif current_key == "e":
                glRotatef(1, 0, 0, 1)
            elif current_key == "space":
                flipped = not(flipped)
            prev_key_states[current_key] = True
        if event.type == pygame.KEYUP:
            prev_key_states[pygame.key.name(event.key)] = False

    if prev_key_states["w"]:
        glRotatef(1, 1, 0, 0)
    if prev_key_states["a"]:
        glRotatef(1, 0, 1, 0)
    if prev_key_states["s"]:
        glRotatef(1, -1, 0, 0)
    if prev_key_states["d"]:
        glRotatef(1, 0, -1, 0)
    if prev_key_states["q"]:
        glRotatef(1, 0, 0, -1)
    if prev_key_states["e"]:
        glRotatef(1, 0, 0, 1)

    glLineWidth(1)
    glBegin(GL_LINES)
    if flipped:
        glColor3fv((colours["cyan"]))
        glVertex3fv((0, 0, 0))
        glVertex3fv((-l, 0, 0))
        glColor3fv((colours["magenta"]))
        glVertex3fv((0, 0, 0))
        glVertex3fv((0, -l, 0))
        glColor3fv((colours["yellow"]))
        glVertex3fv((0, 0, 0))
        glVertex3fv((0, 0, -l))
    else:
        glColor3fv((colours["red"]))
        glVertex3fv((0, 0, 0))
        glVertex3fv((l, 0, 0))
        glColor3fv((colours["green"]))
        glVertex3fv((0, 0, 0))
        glVertex3fv((0, l, 0))
        glColor3fv((colours["blue"]))
        glVertex3fv((0, 0, 0))
        glVertex3fv((0, 0, l))
    glEnd()

    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3fv((colours["orange"]))
    glVertex3fv((0, 0, 0))
    glVertex3fv((1.6, 0.8, 1.2))
    glColor3fv((colours["white"]))
    glVertex3fv((0, 0, 0))
    glVertex3fv((1, 1.5, 2))
    if flipped:
        glColor3fv((colours["grey"]))
        glVertex3fv((0, 0, 0))
        glVertex3fv((0.2, 2, -1.6))
    else:
        glColor3fv((colours["grey"]))
        glVertex3fv((0, 0, 0))
        glVertex3fv((-0.2, -2, 1.6))
    glEnd()

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()