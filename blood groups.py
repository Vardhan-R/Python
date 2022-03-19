import pygame, random, time

pygame.init()

all_old_orgs = []
all_new_orgs = []
alleles = ["A", "B", "O"]
show_genotype = -1
width = 800
height = 600
black = (0, 0, 0)
running = True
AA = ["A", "A"]
AB = ["A", "B"]
AO = ["A", "O"]
BB = ["B", "B"]
BO = ["B", "O"]
OO = ["O", "O"]
AA_orgs = 0
AB_orgs = 0
AO_orgs = 0
BB_orgs = 0
BO_orgs = 0
OO_orgs = 0

class Organism:
    def __init__(self, a1, a2): self.alleles = sorted([a1, a2])

def show():
    global AA_orgs, AB_orgs, AO_orgs, BB_orgs, BO_orgs, OO_orgs
    for m in all_old_orgs:
        if m.alleles == AA: AA_orgs += 1
        elif m.alleles == AB: AB_orgs += 1
        elif m.alleles == AO: AO_orgs += 1
        elif m.alleles == BB: BB_orgs += 1
        elif m.alleles == BO: BO_orgs += 1
        else: OO_orgs += 1

    if show_genotype == 1:
        for m in range(AA_orgs): pygame.draw.circle(scrn, (255, 0, 0), (4, height - 4 * (2 * m + 1)), 4)
        for m in range(AO_orgs): pygame.draw.circle(scrn, (0, 255, 0), (12, height - 4 * (2 * m + 1)), 4)
        for m in range(AB_orgs): pygame.draw.circle(scrn, (255, 0, 255), (20, height - 4 * (2 * m + 1)), 4)
        for m in range(BB_orgs): pygame.draw.circle(scrn, (0, 0, 255), (28, height - 4 * (2 * m + 1)), 4)
        for m in range(BO_orgs): pygame.draw.circle(scrn, (255, 255, 0), (36, height - 4 * (2 * m + 1)), 4)
        for m in range(OO_orgs): pygame.draw.circle(scrn, (255, 255, 255), (44, height - 4 * (2 * m + 1)), 4)
    else:
        for m in range(AA_orgs + AO_orgs): pygame.draw.circle(scrn, (255, 0, 0), (4, height - 4 * (2 * m + 1)), 4)
        for m in range(AB_orgs): pygame.draw.circle(scrn, (255, 0, 255), (12, height - 4 * (2 * m + 1)), 4)
        for m in range(BB_orgs + BO_orgs): pygame.draw.circle(scrn, (0, 0, 255), (20, height - 4 * (2 * m + 1)), 4)
        for m in range(OO_orgs): pygame.draw.circle(scrn, (255, 255, 255), (28, height - 4 * (2 * m + 1)), 4)
    AA_orgs = 0
    AB_orgs = 0
    AO_orgs = 0
    BB_orgs = 0
    BO_orgs = 0
    OO_orgs = 0

def rep(org1, org2):
    global all_new_orgs
    temp_list = []
    c = random.choice([1, 2])
    if c == 1: temp_list.append(org1.alleles[0])
    else: temp_list.append(org1.alleles[1])
    c = random.choice([1, 2])
    if c == 1: temp_list.append(org2.alleles[0])
    else: temp_list.append(org2.alleles[1])
    all_new_orgs.append(Organism(temp_list[0], temp_list[1]))

for i in range(75):
    temp_allele1 = random.choice([0, 1, 2])
    temp_allele2 = random.choice([0, 1, 2])
    all_old_orgs.append(Organism(alleles[temp_allele1], alleles[temp_allele2]))

scrn = pygame.display.set_mode((width, height))

while running:
    scrn.fill(black)

    show()

    for i in range(75): rep(all_old_orgs[random.randrange(0, len(all_old_orgs))], all_old_orgs[random.randrange(0, len(all_old_orgs))])
    all_old_orgs = all_new_orgs.copy()
    all_new_orgs.clear()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN and pygame.key.name(event.key) == "space": show_genotype *= -1

    pygame.display.update()
    time.sleep(0.1)

pygame.quit()