import pygame, time

pygame.init()

running = True
width = 800
height = 600
c = 0
tm = []
typed = ""

scrn = pygame.display.set_mode((width, height))
font_size = 12
font = pygame.font.Font("freesansbold.ttf", font_size)

while running:
    scrn.fill((200, 200, 250))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            typed += pygame.key.name(event.key)
            if len(tm) < 2:
                tm.append(time.process_time())
            else:
                tm[1] = time.process_time()
            c += 1
    text = font.render(typed, True, (0, 0, 0))
    scrn.blit(text, (1, 1))

    pygame.display.update()

pygame.quit()
print(c / (tm[-1] - tm[0]))