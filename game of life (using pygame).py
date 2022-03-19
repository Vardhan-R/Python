import math, pygame, time

pygame.init()

width = 600
height = 600
rows = 15
cols = 15
temp_row = []
board = []
count = []
running = True
playing = -1

scrn = pygame.display.set_mode((width, height))

def grid(rows, cols):
    for m in range(rows):
        pygame.draw.line(scrn, (0, 0, 0), (0, m * height / rows), (width, m * height / rows))
    for m in range(cols):
        pygame.draw.line(scrn, (0, 0, 0), (m * width / cols, 0), (m * width / cols, height), 1)

for i in range(cols):
    temp_row.append(0)
for i in range(rows):
    board.append(temp_row.copy())
    count.append(temp_row.copy())

while running:
    scrn.fill((255, 255, 255))
    grid(rows, cols)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if pygame.mouse.get_pressed()[0] and playing == -1:
            x = math.floor(pygame.mouse.get_pos()[0] * cols / width)
            y = math.floor(pygame.mouse.get_pos()[1] * rows / height)
            if board[y][x]: board[y][x] = 0
            else: board[y][x] = 1

        if event.type == pygame.KEYDOWN: # toggle play and pause
            if pygame.key.name(event.key) == "space": playing *= -1

        if playing == 1:
            for i in range(rows):
                for j in range(cols):
                    cnt = 0
                    for k in range(i - 1, i + 2):
                        for l in range(j - 1, j + 2):
                            try:
                                if (k != i or l != j) and board[k][l]: cnt += 1
                            except:
                                pass
                    count[i][j] = cnt
            for i in range(rows):
                for j in range(cols):
                    if not(board[i][j]) and count[i][j] == 3: board[i][j] = 1
                    elif count[i][j] < 2 or count[i][j] > 3: board[i][j] = 0

            time.sleep(1)

    for i in range(rows):
        for j in range(cols):
            pygame.draw.rect(scrn, (255, 255, 255 * (1 - board[i][j])), pygame.Rect(j * width / cols + 1, i * height / rows + 1, width / cols - 1, height / rows - 1))

    pygame.display.update()

pygame.quit()
