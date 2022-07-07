import numpy as np, pygame

# right (2 ^ 0); down (2 ^ 1); left (2 ^ 2); up (2 ^ 3); 1 (2 ^ 4)
dim = 20 # dim ==> dimension
rng = np.random.default_rng()
width = 600
height = 600
running = True
black = (0, 0, 0)
white = (255, 255, 255)
px_size = width // dim // 3

scrn = pygame.display.set_mode((width, height))

def calcEntropy():
    global entropy_arr
    for i in range(dim):
        for j in range(dim):
            if maze[i][j] == -1:
                for k in range(17, 32):
                    entropy_arr[i][j] += int(checkAdjecents(i, j, k))
            else:
                entropy_arr[i][j] = 99

def checkAdjecents(row, col, i):
    current_tile_bin = bin(i)
    if col + 1 < dim: # right
        a = (current_tile_bin[-1] == bin(maze[row][col + 1])[-3]) or (maze[row][col + 1] == -1)
    else:
        a = not(int(current_tile_bin[-1]))
    if row + 1 < dim: # down
        b = (current_tile_bin[-2] == bin(maze[row + 1][col])[-4]) or (maze[row + 1][col] == -1)
    else:
        b = not(int(current_tile_bin[-2]))
    if col - 1 >= 0: # left
        c = (current_tile_bin[-3] == bin(maze[row][col - 1])[-1]) or (maze[row][col - 1] == -1)
    else:
        c = not(int(current_tile_bin[-3]))
    if row - 1 >= 0: # up
        d = (current_tile_bin[-4] == bin(maze[row - 1][col])[-2]) or (maze[row - 1][col] == -1)
    else:
        d = not(int(current_tile_bin[-4]))
    return a and b and c and d

maze = np.full((dim, dim), -1)

for i in range(dim ** 2):
    entropy_arr = np.full((dim, dim), 0)

    calcEntropy()

    pos = np.argmin(entropy_arr)
    all_choices = []
    for j in range(17, 32):
        if checkAdjecents(pos // dim, pos % dim, j): # returns a and b and c and d
            all_choices.append(j)

    if all_choices:
        maze[pos // dim][pos % dim] = rng.choice(all_choices)
    else:
        maze[pos // dim][pos % dim] = 16

while running:
    scrn.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(dim):
        for j in range(dim):
            tile_bin = bin(maze[i][j])

            if int(tile_bin[-1]): # right
                pygame.draw.rect(scrn, white, pygame.Rect((3 * j + 2) * px_size, (3 * i + 1) * px_size, px_size, px_size))
            if int(tile_bin[-2]): # down
                pygame.draw.rect(scrn, white, pygame.Rect((3 * j + 1) * px_size, (3 * i + 2) * px_size, px_size, px_size))
            if int(tile_bin[-3]): # left
                pygame.draw.rect(scrn, white, pygame.Rect((3 * j) * px_size, (3 * i + 1) * px_size, px_size, px_size))
            if int(tile_bin[-4]): # up
                pygame.draw.rect(scrn, white, pygame.Rect((3 * j + 1) * px_size, (3 * i) * px_size, px_size, px_size))
            if maze[i][j] > 16: # centre
                pygame.draw.rect(scrn, white, pygame.Rect((3 * j + 1) * px_size, (3 * i + 1) * px_size, px_size, px_size))

    pygame.display.update()

pygame.quit()
