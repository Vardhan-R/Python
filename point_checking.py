import math, pygame, random, time
import import_vectors as vect

pygame.init()

width = 800
height = 600
running = True
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
pts = [(213, 361), (211, 294), (495, 314), (516, 412), (365, 447)]
test_pt = vect.Vector(0, 0)
pmb1s = False

scrn = pygame.display.set_mode((width, height))

for i in range(len(pts)):
    pts[i] = vect.Vector(pts[i][0], pts[i][1])

while running:
    scrn.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_pressed()[0]:
        # print(pygame.mouse.get_pos())
        if not(pmb1s):
            test_pt = vect.Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            angle = 0
            for i in range(len(pts)):
                angle += vect.angBetween(vect.sub(test_pt, pts[i - 1]), vect.sub(test_pt, pts[i]))
            print(round(angle, 5) == round(2 * math.pi, 5))
            pmb1s = True
    else:
        pmb1s = False

    for i in range(len(pts)):
        pygame.draw.circle(scrn, blue, (pts[i].x, pts[i].y), 2)
        pygame.draw.line(scrn, green, (pts[i - 1].x, pts[i - 1].y), (pts[i].x, pts[i].y))

    pygame.display.update()

pygame.quit()