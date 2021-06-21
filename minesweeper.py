import math, pygame, random

pygame.init()

mines = 10
rows = 10
cols = 10
board = []
width = 600
height = 600
cell_states = []
mines_guessed = 0
running = True

def grid(a, b):
    for m in range(a):
        pygame.draw.line(scrn, (0, 0, 0), (0, m * height / a), (width, m * height / a))
    for m in range(b):
        pygame.draw.line(scrn, (0, 0, 0), (m * width / b, 0), (m * width / b, height))

# creating the board
for i in range(rows):
    board.append([])
    cell_states.append([])
for i in range(rows):
    for j in range(cols):
        board[i].append("")
        cell_states[i].append(0)

# adding mines to the board
for i in range(mines):
    row = random.randrange(0, rows)
    col = random.randrange(0, cols)
    while board[row][col] == "m":
        row = random.randrange(0, rows)
        col = random.randrange(0, cols)
    board[row][col] = "m"

for i in range(rows):
    for j in range(cols):
        mines_cnt = 0
        if board[i][j] != "m":
            for k in range(i - 1, i + 2):
                for l in range(j - 1, j + 2):
                    if (k != i or l != j) and 0 <= k < rows and 0 <= l < cols and board[k][l] == "m":
                        mines_cnt += 1
            board[i][j] = mines_cnt

scrn = pygame.display.set_mode((width, height))
pygame.display.set_caption("Minesweeper")
font_size = 24
font = pygame.font.Font("freesansbold.ttf", font_size)
flag = pygame.image.load(r'pygame_images/flag.png')
qm = pygame.image.load(r'pygame_images/question_mark.png')

while running:
    # game over check
    b = True
    for i in range(rows):
        if not(b):
            break
        for j in range(cols):
            if board[i][j] != "m" and cell_states[i][j] != 1:
                b = False
                break
    if b:
        break

    # display
    scrn.fill((200, 200, 200))
    grid(rows, cols)
    for i in range(rows):
        for j in range(cols):
            if cell_states[i][j] == 1:
                if board[i][j] == 0:
                    pygame.draw.rect(scrn, (150, 150, 150), pygame.Rect(j * width / cols + 1, i * height / rows + 1, width / cols - 1, height / rows - 1))
                else:
                    text = font.render(str(board[i][j]), True, (100, 100, 255))
                    scrn.blit(text, ((j + 1 / 2) * width / cols - font_size / 2, (i + 1 / 2) * height / rows - font_size / 4))

                if board[i][j] == "m":
                    running = False

            elif cell_states[i][j] == 2:
                scrn.blit(flag, ((j + 0.45) * width / cols - font_size / 2, (i + 0.36) * height / rows - font_size / 4))
                mines_guessed += 1

            elif cell_states[i][j] == 3:
                scrn.blit(qm, ((j + 0.4) * width / cols - font_size / 2, (i + 0.35) * height / rows - font_size / 4))

    for event in pygame.event.get():
        # exit
        if event.type == pygame.QUIT:
            running = False

        # click
        if pygame.mouse.get_pressed()[0]:
            x = math.floor(pygame.mouse.get_pos()[0] * cols / width)
            y = math.floor(pygame.mouse.get_pos()[1] * rows / height)
            cell_states[y][x] = 1
            expand = True

        if pygame.mouse.get_pressed()[2]:
            x = math.floor(pygame.mouse.get_pos()[0] * cols / width)
            y = math.floor(pygame.mouse.get_pos()[1] * rows / height)
            if cell_states[y][x] == 0:
                cell_states[y][x] = 2
            elif cell_states[y][x] == 2:
                cell_states[y][x] = 3
            elif cell_states[y][x] == 3:
                cell_states[y][x] = 0

        # expand
        for i in range(rows):
            for j in range(cols):
                if cell_states[i][j] == 1 and board[i][j] == 0:
                    for k in range(i - 1, i + 2):
                        for l in range(j - 1, j + 2):
                            if (k != i or l != j) and 0 <= k < rows and 0 <= l < cols:
                                cell_states[k][l] = True
        else:
            expand = False

    mines_text = font.render(str(mines - mines_guessed), True, (255, 100, 100))
    scrn.blit(mines_text, (1, 1))
    mines_guessed = 0

    pygame.display.update()

pygame.quit()
if running:
    print("You Won!")
else:
    quit()
