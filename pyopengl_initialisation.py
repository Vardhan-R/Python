from OpenGL.GL import *
from OpenGL.GLU import *
import pygame

pygame.init()

width = 800
height = 600
running = True

pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.OPENGL)

gluPerspective(45, width / height, 0.1, 50)

glTranslatef(0, 0, -8)

while running:
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()