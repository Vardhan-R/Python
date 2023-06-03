from built_modules import import_vectors as vect
from manim import *
import numpy as np, pygame, time

pygame.init()

width = 600
height = 600
running = True
density = 40
eta = 0.3
all_h_lines_vel = np.zeros((density, density))
all_v_lines_vel = np.zeros((density, density))

class Square:
    def __init__(self, pos: vect.Vector, vel: vect.Vector):
        self.clr = (vel.mag / 4, 0, 0)
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

def v_para(v: float | int) -> float:
    return (3 - 2 * eta) * v / 3

def v_perp(v: float | int, direction: int = 1) -> float:
    return direction * eta * v / 3

# all_h_lines_vel[density // 2][density // 2] = 1

l = 3
for i in range(l):
    all_v_lines_vel[density // 2][density // 2 + i] = 1
    all_v_lines_vel[density // 2 + l][density // 2 + i] = -1
    all_h_lines_vel[density // 2 + i][density // 2] = -1
    all_h_lines_vel[density // 2 + i][density // 2 + l] = 1

while running:
    scrn.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update
    all_h_lines_induced_vel = np.zeros((density, density))
    all_v_lines_induced_vel = np.zeros((density, density))

    for i in range(density):
        for j in range(density):
            # h
            all_h_lines_induced_vel[i - 1][j] += v_para(all_h_lines_vel[i][j]) # t
            all_h_lines_induced_vel[i + 1 - (i + 1) // density * density][j] += v_para(all_h_lines_vel[i][j]) # b
            all_v_lines_induced_vel[i - 1][j] += v_perp(all_h_lines_vel[i][j]) # tl
            all_v_lines_induced_vel[i - 1][j + 1 - (j + 1) // density * density] += v_perp(all_h_lines_vel[i][j], -1) # tr
            all_v_lines_induced_vel[i][j] += v_perp(all_h_lines_vel[i][j], -1) # bl
            all_v_lines_induced_vel[i][j + 1 - (j + 1) // density * density] += v_perp(all_h_lines_vel[i][j]) # br

            # v
            all_v_lines_induced_vel[i][j - 1] += v_para(all_v_lines_vel[i][j]) # l
            all_v_lines_induced_vel[i][j + 1 - (j + 1) // density * density] += v_para(all_v_lines_vel[i][j]) # r
            all_h_lines_induced_vel[i][j - 1] += v_perp(all_v_lines_vel[i][j]) # tl
            all_h_lines_induced_vel[i][j] += v_perp(all_v_lines_vel[i][j], -1) # tr
            all_h_lines_induced_vel[i + 1 - (i + 1) // density * density][j - 1] += v_perp(all_v_lines_vel[i][j], -1) # bl
            all_h_lines_induced_vel[i + 1 - (i + 1) // density * density][j] += v_perp(all_v_lines_vel[i][j]) # br

    all_h_lines_vel += all_h_lines_induced_vel
    all_v_lines_vel += all_v_lines_induced_vel
    # all_h_lines_vel /= 2.5
    # all_v_lines_vel /= 2.5
    print(np.max(all_h_lines_vel), np.max(all_v_lines_vel))

    # display
    for i in range(density):
        for j in range(density):
            arrow(vect.Vector((j + 1 / 2) * width / density, (i + 1 / 2) * height / density), vect.Vector(all_v_lines_vel[i][j] + all_v_lines_vel[i][j + 1 - (j + 1) // density * density], all_h_lines_vel[i][j] + all_h_lines_vel[i + 1 - (i + 1) // density * density][j]))

    pygame.display.update()
    time.sleep(0.1)

pygame.quit()