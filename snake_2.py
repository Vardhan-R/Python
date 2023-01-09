from manim import *
import numpy as np, pygame, random

pygame.init()

width = 600
height = 600
running = True
density = 20
t = 0
pause_tm = 5000
body = [(density // 2, density // 2)]
vel = (0, -1)
food = (random.randrange(0, density), random.randrange(0, density))

scrn = pygame.display.set_mode((width, height))

def grid(width, height, density):
    for m in range(density):
        pygame.draw.line(scrn, (255, 255, 255), (m * width / density, 0), (m * width / density, height))
        pygame.draw.line(scrn, (255, 255, 255), (0, m * height / density), (width, m * height / density))

while running:
    scrn.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            current_key = pygame.key.name(event.key)
            if current_key == "w":
                vel = (0, -1)
            elif current_key == "a":
                vel = (-1, 0)
            elif current_key == "s":
                vel = (0, 1)
            elif current_key == "d":
                vel = (1, 0)

    if not t:
        # food detection
        if body[0] == food:
            body.append(body[-1])
            food = (random.randrange(0, density), random.randrange(0, density))

        # move snake
        body.insert(0, ((body[0][0] + vel[0]) % density, (body[0][1] + vel[1]) % density))
        body.pop()

        # collision detection
        a, cnts = np.unique(np.array(body), axis = 0, return_counts = True)
        for i in cnts:
            if i != 1:
                running = False
                break

        # display
        grid(width, height, density)
        for i in body:
            pygame.draw.rect(scrn, (0, 255, 0), pygame.Rect(i[0] * width / density, i[1] * height / density, width / density, height / density))
        pygame.draw.rect(scrn, (255, 0, 0), pygame.Rect(food[0] * width / density, food[1] * height / density, width / density, height / density))

        pygame.display.update()

    t = (t + 1) % pause_tm

pygame.quit()

# list of body pieces pos
# vel is initialised
# first element is initally first element + vel
# delete last element
# collision detection