import pygame, random

pygame.init()

width = 600
height = 600
density = 20
canvas = (width, height)
running = True
headX = width / 2
headY = height / 2
bodyX = [width / 2]
bodyY = [height * (1 / 2 + 1 / density)]
velX = 0
velY = -height / density
boost = False
cnt = 0
move = True
tm = 400

def grid():
    for m in range(density):
        pygame.draw.line(scrn, (255, 255, 255), (m * width / density, 0), (m * width / density, height), 1)
        pygame.draw.line(scrn, (255, 255, 255), (0, m * height / density), (width, m * height / density))

def generateFood():
    global foodX, foodY
    foodX = (0.5 + random.randrange(0, density)) * (width / density)
    foodY = (0.5 + random.randrange(0, density)) * (height / density)

generateFood()

icon = pygame.image.load(r'C:\Users\Dr. Mrunalini\Desktop\Vardhan\pygame_images\snake_icon.png')
spd = pygame.image.load(r'C:\Users\Dr. Mrunalini\Desktop\Vardhan\pygame_images\spd_24_px.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Snake")
scrn = pygame.display.set_mode(canvas)
font = pygame.font.Font('freesansbold.ttf', 24)
text = font.render("Score: " + str(len(bodyX) - 1), True, (255, 255, 0))

while running:
    cnt += 1
    scrn.fill((0, 0, 0))
    grid()
    if boost:
        scrn.blit(spd, (2, height - 25))
    pygame.draw.circle(scrn, (255, 0, 0), (foodX, foodY), 0.35 * width / density)
    pygame.draw.rect(scrn, (0, 255, 0), pygame.Rect(headX, headY, width / density, height / density))
    for i in range(len(bodyX)):
        pygame.draw.rect(scrn, (0, 150, 0), pygame.Rect(bodyX[i], bodyY[i], width / density, height / density))
    scrn.blit(text, (1, 1))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == "space":
                tm = 100
                boost = True

            if move:
                if pygame.key.name(event.key) == "w" and velY == 0:
                    velX = 0
                    velY = -height / density
                elif pygame.key.name(event.key) == "a" and velX == 0:
                    velX = -width / density
                    velY = 0
                elif pygame.key.name(event.key) == "s" and velY == 0:
                    velX = 0
                    velY = height / density
                elif pygame.key.name(event.key) == "d" and velX == 0:
                    velX = width / density
                    velY = 0
                move = False

        if event.type == pygame.KEYUP and pygame.key.name(event.key) == "space":
            tm = 400
            boost = False

    if cnt % tm == 0:
        bodyX.insert(0, headX)
        bodyY.insert(0, headY)
        headX += velX
        headY += velY
        cnt = 0
        move = True

        if headX < 0 or headX >= width or headY < 0 or headY >= height:
            running = False

        if headX + 0.5 * width / density == foodX and headY + 0.5 * height / density == foodY:
            generateFood()
            text = font.render("Score: " + str(len(bodyX) - 1), True, (255, 255, 0))
        else:
            bodyX.pop()
            bodyY.pop()

        for i in range(len(bodyX)):
            if headX == bodyX[i] and headY == bodyY[i]:
                running = False

    pygame.display.update()

pygame.quit()
quit()