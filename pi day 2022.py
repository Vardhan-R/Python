import math, pygame, random, time

pygame.init()

width = 800
height = 600
running = False
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
n = 1000
radius = min(width / 2, height / 2)
coprime_lst = []

def gcd(n_1, n_2):
    a = max(n_1, n_2)
    b = min(n_1, n_2)
    q = 0
    r = a
    while r >= b:
        q += 1
        r = a - q * b
    if r == 0:
        return b
    else:        
        return gcd(b, r)

scrn = pygame.display.set_mode((width, height))
font = pygame.font.SysFont("Courier New", 24)

for i in range(1, n + 1):
    for j in range(i, n + 1):
        if gcd(i, j) == 1:
            coprime_lst.append((i, j))

# print(coprime_lst)
print(math.sqrt(3 * (n - 1) * n / len(coprime_lst)))

while running:
    scrn.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.circle(scrn, white, (width / 2, height / 2), radius, 1)

    for i in range(n):
        text = font.render(str(i + 1), True, blue)
        scrn.blit(text, (width / 2 + radius * math.cos(2 * math.pi * i / n - math.pi / 2) - 7, height / 2 + radius * math.sin(2 * math.pi * i / n - math.pi / 2) - 11))

    for i in coprime_lst:
        pygame.draw.line(scrn, red, (width / 2 + radius * math.cos(2 * math.pi * (i[0] - 1) / n - math.pi / 2), height / 2 + radius * math.sin(2 * math.pi * (i[0] - 1) / n - math.pi / 2)), (width / 2 + radius * math.cos(2 * math.pi * (i[1] - 1) / n - math.pi / 2), height / 2 + radius * math.sin(2 * math.pi * (i[1] - 1) / n - math.pi / 2)))

    pygame.display.update()

pygame.quit()