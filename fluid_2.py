from built_modules import import_vectors as vect
from manim import *
import numpy as np, pygame, time

pygame.init()

width = 600
height = 600
running = True
density = 40
eta = 1
# all_h_lines_vel = np.zeros((density, density))
# all_v_lines_vel = np.zeros((density, density))
all_squares_vel = np.zeros((density, density, 2))
all_squares_induced_vel = np.zeros((density, density, 2))

class Square:
    def __init__(self, vel: vect.Vector):
        # self.clr = (vel.mag / 4, 0, 0)
        self.vel = vel
        self.induced_vel = vect.Vector()

    def show(self):
        pygame.draw.rect(scrn, self.clr, pygame.Rect(self.pos.x, self.pos.y, width / density, height / density))

scrn = pygame.display.set_mode((width, height))

def arrow(pos: vect.Vector, vel: vect.Vector):
    try:
        vel = vel.setMag(min(width, height) / density / 3 * np.tanh(vel.mag()))
    except:
        pass
    f_vect = vect.add(pos, vel)
    i_vect = vect.sub(pos, vel)
    pygame.draw.line(scrn, BLACK, (i_vect.x, i_vect.y), (f_vect.x, f_vect.y), 1)
    pygame.draw.circle(scrn, BLACK, (f_vect.x, f_vect.y), 3)

def sigmoid(x: float | int) -> float:
    return 1 / (1 + np.e ** (-x))

def vPara(v: float | int) -> float:
    return (3 - 2 * eta) * v / 3

def vPerp(v: float | int) -> float:
    return eta * v / 3

all_squares_vel[density // 2][density // 2] = np.array([0, 1])

# l = 3
# for i in range(l):
#     all_v_lines_vel[density // 2][density // 2 + i] = 1

while running:
    scrn.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update
    # all_squares_induced_vel = np.zeros((density, density, 2))

    for i in range(-1, density - 1):
        for j in range(-1, density - 1):
            # grid = all_squares_vel[(i - 1):(i + 2), (j - 1):(j + 2)] - all_squares_vel[i][j]
            grid = np.array([[(0, 0), all_squares_vel[i - 1][j], (0, 0)],
                             [all_squares_vel[i][j - 1], (0, 0), all_squares_vel[i][j + 1]],
                             [(0, 0), all_squares_vel[i + 1][j], (0, 0)]]) - all_squares_vel[i][j]
            # div = np.array(all_squares_vel[i][j + 1][0] - all_squares_vel[i][j - 1][0])
            all_squares_induced_vel[i][j][0] = (grid[1][0][0] + grid[1][2][0] + vPara(grid[0][1][0] + grid[2][1][0]) + vPerp(grid[1][2][1] - grid[1][0][1])) / 3
            all_squares_induced_vel[i][j][1] = (grid[0][1][1] + grid[2][1][1] + vPara(grid[1][0][1] + grid[1][2][1]) + vPerp(grid[2][1][0] - grid[0][1][0])) / 3
            # all_squares_induced_vel[i][j][1] += vPara(all_squares_vel[i + 1][j][1] - all_squares_vel[i - 1][j][1]) + vPerp(all_squares_vel[i - 1][j][0] + all_squares_vel[i + 1][j][0])

    all_squares_vel = all_squares_induced_vel
    # all_h_lines_vel /= 2.5
    # all_v_lines_vel /= 2.5
    print(np.max(all_squares_vel[:, :, 0]), np.max(all_squares_vel[:, :, 1]))

    # display
    for i in range(density):
        for j in range(density):
            arrow(vect.Vector((j + 1 / 2) * width / density, (i + 1 / 2) * height / density), vect.Vector(all_squares_vel[i][j][0], all_squares_vel[i][j][1]))

    pygame.display.update()
    time.sleep(0.1)

pygame.quit()