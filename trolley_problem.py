from built_modules import import_vectors as vect
from copy import deepcopy
from manim import *
import pygame, random, time

pygame.init()

width = 800
height = 600
running = True
n = 100
dt = 0.01
pos = vect.Vector(width / 2, height / 2)
vel = vect.Vector(0, 0)
moves = 500
destination = vect.Vector(3 * width / 4, height / 2)
l_lim = 0.45
u_lim = 0.55

class Organism:
    def __init__(self):
        self.pos = vect.Vector(width / 4, height / 2)
        self.vel = vect.Vector(0, 0)
        self.acc = [random.randrange(0, round(2000 * np.pi)) / 1000 for _ in range(moves)]
        # self.score = width / 2
        self.scores = np.zeros(moves)

scrn = pygame.display.set_mode((width, height))

def accMag(pos: vect.Vector) -> float:
    if l_lim * height < pos.y < u_lim *  height:
        return 0.98
    else:
        return 9.8

def mutate(org: Organism, mutation_rate: float | int = 0.01) -> None:
    for i in range(moves):
        org.acc[i] = np.random.choice([random.randrange(0, round(2000 * np.pi)) / 1000, org.acc[i]], p=[mutation_rate, 1 - mutation_rate])

all_orgs = [Organism() for _ in range(n)]

while running:
    scrn.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    min_score = width * height
    min_score_index = 0
    for i in range(n):
        for j in range(moves):
            acc_mag = accMag(all_orgs[i].pos) * dt
            all_orgs[i].vel.x += acc_mag * np.cos(all_orgs[i].acc[j])
            all_orgs[i].vel.y += acc_mag * np.sin(all_orgs[i].acc[j])
            all_orgs[i].pos.x += all_orgs[i].vel.x
            all_orgs[i].pos.y += all_orgs[i].vel.y
            all_orgs[i].scores[j] = np.sqrt((destination.x - all_orgs[i].pos.x) ** 2 + (destination.y - all_orgs[i].pos.y) ** 2)

            pygame.draw.circle(scrn, BLUE, (all_orgs[i].pos.x, all_orgs[i].pos.y), 1)

        curr_score = np.min(all_orgs[i].scores)
        if curr_score < min_score:
            min_score = curr_score
            min_score_index = i

        pygame.draw.line(scrn, RED, (0, l_lim * height), (width, l_lim * height))
        pygame.draw.line(scrn, RED, (0, u_lim * height), (width, u_lim * height))

        pygame.display.update()

    # all_orgs[min_score_index].pos = vect.Vector(width / 4, height / 2)
    # all_orgs[min_score_index].vel = vect.Vector(0, 0)
    # all_orgs[min_score_index].score = width / 2
    # all_orgs
    # all_orgs = [deepcopy(all_orgs[min_score_index]) for _ in range(n)]
    for i in all_orgs:
        i.pos = vect.Vector(width / 4, height / 2)
        i.vel = vect.Vector(0, 0)
        i.acc = deepcopy(all_orgs[min_score_index].acc)
        i.scores = np.zeros(moves)
        mutate(i, 0.001)

    time.sleep(1)

pygame.quit()