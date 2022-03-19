import math, pygame, random, time

pygame.init()

width = 800
height = 600
black = (0, 0, 0)
green = (0, 255, 0)
running = True

scrn = pygame.display.set_mode((width, height))

all_pts = []
density = 200
for i in range(4 * density):
    n = 0.5
    all_pts.append([])
    for j in range(density):
        n = i * n * (1 - n) / density
        if j > density / 2: all_pts[i].append(n)

while running:
    scrn.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if pygame.mouse.get_pressed()[0]: print(pygame.mouse.get_pos()[0] / density, 1 - pygame.mouse.get_pos()[1] / height)

    for i in range(len(all_pts)):
        for j in all_pts[i]:
            scrn.set_at((i, round(height * (1 - j))), green)

    pygame.display.update()

pygame.quit()