from manim import *
import pygame

pygame.init()

width = 800
height = 600
running = True

# define classes here

scrn = pygame.display.set_mode((width, height))

# define functions here

while running:
    scrn.fill((255, 255, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()