import pygame, time

pygame.init()

k = []
rec = True
tm = []
alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
width = 800
height = 600
black = (0, 0, 0)
white = (255, 255, 255)
blue = (100, 100, 255)
running = True

scrn = pygame.display.set_mode((width, height))

font = pygame.font.Font("freesansbold.ttf", 24)

def displayKeyboard():
    pygame.draw.rect(scrn, black, pygame.Rect(0, height - width / 26, width, width / 26))
    for m in range(26):
        # pygame.draw.rect(scrn, black, pygame.Rect(m * width / 26, height - width / 26, width / 26, width / 26))
        pygame.draw.line(scrn, white, (m * width / 26, height - width / 26), (m * width / 26, height))
        text = font.render(chr(m + 97), True, blue)
        scrn.blit(text, (width / 52 * (2 * m + 1) - 5, height - width / 27))

def replay():
    global k, tm

    for m in range(len(k)):
        if tm[m] < height - width / 26 - 10:
            pygame.draw.rect(scrn, blue, pygame.Rect((ord(k[m]) - 97) * width / 26, tm[m], width / 26, 10))
            tm[m] += 0.2 # distance travelled in 1 / 64 seconds

tm.append(time.process_time())
tm.clear()

while running:
    scrn.fill(white)
    displayKeyboard()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if rec:
                if pygame.key.name(event.key) == "1":
                    for i in range(len(tm)):
                        tm[i] -= 500
                    rec = False
                tm.append(height - 64 * time.process_time() - 10)
                k.append(pygame.key.name(event.key))

    if not(rec):
        print(time.localtime())
        # print(time.process_time())
        replay()

    pygame.display.update()

pygame.quit()

# hv to do line 34 and line 53