import math, pygame, random, time
import import_ann as ann
import import_vectors as vect
import import_geneticalgorithm as ga

pygame.init()

width = 800
height = 600
canvas = (width, height)
running = True
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
white = (255, 255, 255)
orgs_per_gen = 10
car_length = 20
car_width = 15
max_vel = 5
tm = 1
max_tm = 500
mutation_rate = 0.06
gen = 0
# inner_path = [(225, 441), (223, 237), (372, 96), (512, 234), (513, 444)]
# outer_path = [(142, 500), (136, 166), (410, 10), (571, 235), (574, 508)]
# initial_pt = vect.Vector(180, 400)
inner_path = [(213, 361), (211, 294), (495, 314), (516, 412), (365, 447)]
outer_path = [(150, 370), (152, 224), (592, 250), (607, 477), (371, 546)]
initial_pt = vect.Vector(183, 333)
checkpts = []
all_ann = []
all_cars = [] # [pos, orientation, vel, region, dist, crashed, tm, laps]

scrn = pygame.display.set_mode(canvas)
font = pygame.font.Font("freesansbold.ttf", 24)

def collision(a):
    vect_1 = vect.add(a[0], vect.Vector(-car_length / 2, car_width / 2).rotate(a[1]))
    vect_2 = vect.add(a[0], vect.Vector(car_length / 2, car_width / 2).rotate(a[1]))
    vect_3 = vect.add(a[0], vect.Vector(car_length / 2, -car_width / 2).rotate(a[1]))
    vect_4 = vect.add(a[0], vect.Vector(-car_length / 2, -car_width / 2).rotate(a[1]))
    angle_1 = 0
    angle_2 = 0
    angle_3 = 0
    angle_4 = 0
    for i in range(len(inner_path)):
        angle_1 += vect.angBetween(vect.sub(vect_1, inner_path[i - 1]), vect.sub(vect_1, inner_path[i]))
        angle_2 += vect.angBetween(vect.sub(vect_2, inner_path[i - 1]), vect.sub(vect_2, inner_path[i]))
        angle_3 += vect.angBetween(vect.sub(vect_3, inner_path[i - 1]), vect.sub(vect_3, inner_path[i]))
        angle_4 += vect.angBetween(vect.sub(vect_4, inner_path[i - 1]), vect.sub(vect_4, inner_path[i]))
    inner_result = round(angle_1, 5) < round(2 * math.pi, 5) and round(angle_2, 5) < round(2 * math.pi, 5) and round(angle_3, 5) < round(2 * math.pi, 5) and round(angle_4, 5) < round(2 * math.pi, 5)
    angle_1 = 0
    angle_2 = 0
    angle_3 = 0
    angle_4 = 0
    for i in range(len(outer_path)):
        angle_1 += vect.angBetween(vect.sub(vect_1, outer_path[i - 1]), vect.sub(vect_1, outer_path[i]))
        angle_2 += vect.angBetween(vect.sub(vect_2, outer_path[i - 1]), vect.sub(vect_2, outer_path[i]))
        angle_3 += vect.angBetween(vect.sub(vect_3, outer_path[i - 1]), vect.sub(vect_3, outer_path[i]))
        angle_4 += vect.angBetween(vect.sub(vect_4, outer_path[i - 1]), vect.sub(vect_4, outer_path[i]))
    outer_result = round(angle_1, 5) == round(2 * math.pi, 5) and round(angle_2, 5) == round(2 * math.pi, 5) and round(angle_3, 5) == round(2 * math.pi, 5) and round(angle_4, 5) == round(2 * math.pi, 5)
    return(not(inner_result and outer_result))

def getDist(pt_a, pt_b, pt_c, r):
    a = vect.sub(pt_b, pt_c)
    b = vect.sub(pt_a, pt_c)
    c = vect.sub(pt_a, pt_b)
    if round(vect.angBetween(a, b), 5) == round(vect.angBetween(r, a) + vect.angBetween(r, b), 5):
        return [True, vect.cross(a, b).mag() / vect.cross(c, r.normalise()).mag()]
    else:
        return [False]

def getMinDist(c, r):
    all_dist = []
    for i in range(len(inner_path)):
        result = getDist(inner_path[i - 1], inner_path[i], c, r)
        if result[0]:
            all_dist.append(result[1])

    for i in range(len(outer_path)):
        result = getDist(outer_path[i - 1], outer_path[i], c, r)
        if result[0]:
            all_dist.append(result[1])

    return sorted(all_dist)[0]

def generateInputs(a):
    input_lst = []
    min_dist = getMinDist(vect.add(a[0], vect.Vector(car_length / 2, car_width / 2).rotate(a[1])), vect.Vector(1, 0).rotate(a[1]))
    input_lst.append(min_dist)
    v_1 = vect.add(a[0], vect.Vector(car_length / 2, car_width / 2).rotate(a[1]))
    v_2 = vect.add(v_1, vect.Vector(min_dist, 0).rotate(a[1]))
    pygame.draw.line(scrn, yellow, (v_1.x, v_1.y), (v_2.x, v_2.y))

    min_dist = getMinDist(vect.add(a[0], vect.Vector(car_length / 2, car_width / 2).rotate(a[1])), vect.Vector(1, 0).rotate(a[1] + math.pi / 2))
    input_lst.append(min_dist)
    v_1 = vect.add(a[0], vect.Vector(car_length / 2, car_width / 2).rotate(a[1]))
    v_2 = vect.add(v_1, vect.Vector(min_dist, 0).rotate(a[1] + math.pi / 2))
    pygame.draw.line(scrn, yellow, (v_1.x, v_1.y), (v_2.x, v_2.y))

    # min_dist = getMinDist(vect.add(a[0], vect.Vector(-car_length / 2, car_width / 2).rotate(a[1])), vect.Vector(1, 0).rotate(a[1] + math.pi / 2))
    # input_lst.append(min_dist)
    # v_1 = vect.add(a[0], vect.Vector(-car_length / 2, car_width / 2).rotate(a[1]))
    # v_2 = vect.add(v_1, vect.Vector(min_dist, 0).rotate(a[1] + math.pi / 2))
    # pygame.draw.line(scrn, yellow, (v_1.x, v_1.y), (v_2.x, v_2.y))

    # min_dist = getMinDist(vect.add(a[0], vect.Vector(-car_length / 2, car_width / 2).rotate(a[1])), vect.Vector(1, 0).rotate(a[1] + math.pi))
    # input_lst.append(min_dist)
    # v_1 = vect.add(a[0], vect.Vector(-car_length / 2, car_width / 2).rotate(a[1]))
    # v_2 = vect.add(v_1, vect.Vector(min_dist, 0).rotate(a[1] + math.pi))
    # pygame.draw.line(scrn, yellow, (v_1.x, v_1.y), (v_2.x, v_2.y))

    # min_dist = getMinDist(vect.add(a[0], vect.Vector(-car_length / 2, -car_width / 2).rotate(a[1])), vect.Vector(1, 0).rotate(a[1] + math.pi))
    # input_lst.append(min_dist)
    # v_1 = vect.add(a[0], vect.Vector(-car_length / 2, -car_width / 2).rotate(a[1]))
    # v_2 = vect.add(v_1, vect.Vector(min_dist, 0).rotate(a[1] + math.pi))
    # pygame.draw.line(scrn, yellow, (v_1.x, v_1.y), (v_2.x, v_2.y))

    # min_dist = getMinDist(vect.add(a[0], vect.Vector(-car_length / 2, -car_width / 2).rotate(a[1])), vect.Vector(1, 0).rotate(a[1] - math.pi / 2))
    # input_lst.append(min_dist)
    # v_1 = vect.add(a[0], vect.Vector(-car_length / 2, -car_width / 2).rotate(a[1]))
    # v_2 = vect.add(v_1, vect.Vector(min_dist, 0).rotate(a[1] - math.pi / 2))
    # pygame.draw.line(scrn, yellow, (v_1.x, v_1.y), (v_2.x, v_2.y))

    min_dist = getMinDist(vect.add(a[0], vect.Vector(car_length / 2, -car_width / 2).rotate(a[1])), vect.Vector(1, 0).rotate(a[1] - math.pi / 2))
    input_lst.append(min_dist)
    v_1 = vect.add(a[0], vect.Vector(car_length / 2, -car_width / 2).rotate(a[1]))
    v_2 = vect.add(v_1, vect.Vector(min_dist, 0).rotate(a[1] - math.pi / 2))
    pygame.draw.line(scrn, yellow, (v_1.x, v_1.y), (v_2.x, v_2.y))

    # min_dist = getMinDist(vect.add(a[0], vect.Vector(car_length / 2, -car_width / 2).rotate(a[1])), vect.Vector(1, 0).rotate(a[1]))
    # input_lst.append(min_dist)
    # v_1 = vect.add(a[0], vect.Vector(car_length / 2, -car_width / 2).rotate(a[1]))
    # v_2 = vect.add(v_1, vect.Vector(min_dist, 0).rotate(a[1]))
    # pygame.draw.line(scrn, yellow, (v_1.x, v_1.y), (v_2.x, v_2.y))

    input_lst.append(a[1])
    input_lst.append(a[2].x)
    input_lst.append(a[2].y)

    return input_lst

def showAllCars():
    for i in range(len(all_cars)):
        vect_1 = vect.add(all_cars[i][0], vect.Vector(-car_length / 2, car_width / 2).rotate(all_cars[i][1]))
        vect_2 = vect.add(all_cars[i][0], vect.Vector(car_length / 2, car_width / 2).rotate(all_cars[i][1]))
        vect_3 = vect.add(all_cars[i][0], vect.Vector(car_length / 2, -car_width / 2).rotate(all_cars[i][1]))
        vect_4 = vect.add(all_cars[i][0], vect.Vector(-car_length / 2, -car_width / 2).rotate(all_cars[i][1]))
        pygame.draw.line(scrn, red, (vect_1.x, vect_1.y), (vect_2.x, vect_2.y))
        pygame.draw.line(scrn, red, (vect_2.x, vect_2.y), (vect_3.x, vect_3.y))
        pygame.draw.line(scrn, red, (vect_3.x, vect_3.y), (vect_4.x, vect_4.y))
        pygame.draw.line(scrn, red, (vect_4.x, vect_4.y), (vect_1.x, vect_1.y))

def inside(a, l):
    vect_1 = vect.add(a[0], vect.Vector(-car_length / 2, car_width / 2).rotate(a[1]))
    vect_2 = vect.add(a[0], vect.Vector(car_length / 2, car_width / 2).rotate(a[1]))
    vect_3 = vect.add(a[0], vect.Vector(car_length / 2, -car_width / 2).rotate(a[1]))
    vect_4 = vect.add(a[0], vect.Vector(-car_length / 2, -car_width / 2).rotate(a[1]))
    angle_1 = 0
    angle_2 = 0
    angle_3 = 0
    angle_4 = 0
    for i in range(len(l)):
        angle_1 += vect.angBetween(vect.sub(vect_1, l[i - 1]), vect.sub(vect_1, l[i]))
        angle_2 += vect.angBetween(vect.sub(vect_2, l[i - 1]), vect.sub(vect_2, l[i]))
        angle_3 += vect.angBetween(vect.sub(vect_3, l[i - 1]), vect.sub(vect_3, l[i]))
        angle_4 += vect.angBetween(vect.sub(vect_4, l[i - 1]), vect.sub(vect_4, l[i]))
    return round(angle_1, 5) >= round(2 * math.pi, 5) or round(angle_2, 5) >= round(2 * math.pi, 5) or round(angle_3, 5) >= round(2 * math.pi, 5) or round(angle_4, 5) >= round(2 * math.pi, 5)

def getRegion(a):
    for i in range(len(inner_path) - 1):
        if inside(a, [outer_path[i], outer_path[i + 1], inner_path[i + 1], inner_path[i]]):
            return i
    return len(inner_path) - 1

for i in range(len(inner_path)):
    inner_path[i] = vect.Vector(inner_path[i][0], inner_path[i][1])

temp_lst = []
for i in range(len(outer_path)):
    outer_path[i] = vect.Vector(outer_path[i][0], outer_path[i][1])
    checkpts.append(vect.add(inner_path[i], outer_path[i]).mult(1 / 2))
    temp_lst.append(False)
checkpts[0] = initial_pt
temp_lst[0] = True

total_dist = 0
for i in range(len(checkpts)):
    total_dist += vect.sub(checkpts[i], checkpts[i - 1]).mag()

for i in range(orgs_per_gen):
    # all_ann.append(ann.NeuralNetwork([11, 10, 10, 4]))
    # all_ann.append(ann.NeuralNetwork([9, 9, 9, 4]))
    # all_ann.append(ann.NeuralNetwork([7, 8, 8, 4]))
    all_ann.append(ann.NeuralNetwork([6, 7, 7, 4]))
    all_cars.append([initial_pt, -math.pi / 2, vect.Vector(0, 0), temp_lst.copy(), 0, False, 0, 0])

while running:
    scrn.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == "left":
                mutation_rate = max(0, round(mutation_rate - 0.01, 2))
            if pygame.key.name(event.key) == "right":
                mutation_rate = min(1, round(mutation_rate + 0.01, 2))

    text = font.render("Generation: " + str(gen), True, blue)
    scrn.blit(text, (1, 1))
    text = font.render("Time: " + str(tm) + " / " + str(max_tm), True, blue)
    scrn.blit(text, (1, 25))
    text = font.render("Mutation Rate: " + str(mutation_rate), True, blue)
    scrn.blit(text, (1, 49))

    for i in range(len(inner_path)):
        pygame.draw.line(scrn, green, (inner_path[i - 1].x, inner_path[i - 1].y), (inner_path[i].x, inner_path[i].y))

    for i in range(len(outer_path)):
        pygame.draw.line(scrn, green, (outer_path[i - 1].x, outer_path[i - 1].y), (outer_path[i].x, outer_path[i].y))

    for i in checkpts:
        pygame.draw.circle(scrn, blue, (i.x, i.y), 2)

    for i in range(len(all_ann)):
        if not(all_cars[i][5]):
            all_ann[i].feedForward(generateInputs(all_cars[i]))
            best = all_ann[i].best()
            if best == 0:
                all_cars[i][2] = vect.add(all_cars[i][2], vect.Vector(0.01, 0).rotate(all_cars[i][1]))
            elif best == 1:
                all_cars[i][1] -= math.pi / 180
            elif best == 2:
                all_cars[i][2] = vect.add(all_cars[i][2], vect.Vector(-0.01, 0).rotate(all_cars[i][1]))
            else:
                all_cars[i][1] += math.pi / 180

            try:
                all_cars[i][2] = all_cars[i][2].setMag(min(all_cars[i][2].mag(), max_vel))
            except:
                pass
            all_cars[i][0] = vect.add(all_cars[i][0], all_cars[i][2])

            for j in range(len(all_cars[i][3])):
                r = getRegion(all_cars[i])
                if all_cars[i][3][r - 1]:
                    all_cars[i][3][r] = True
                    all_cars[i][3][r - 1] = False
                    if not(r):
                        all_cars[i][7] += 1
                        all_cars[i][4] = 0

            if collision(all_cars[i]) or tm >= max_tm:
                for j in range(len(all_cars[i][3])):
                    if all_cars[i][3][j]:
                        r = j
                        break
                for j in range(r):
                    all_cars[i][4] += vect.sub(checkpts[j + 1], checkpts[j]).mag()
                all_cars[i][4] += vect.sub(all_cars[i][0], checkpts[r]).mag()
                all_cars[i][5] = True
                all_cars[i][6] = tm

    showAllCars()

    gen_dead = True
    for i in all_cars:
        if not(i[5]):
            gen_dead = False
            break

    if gen_dead or tm >= max_tm:
        all_fitnesses = {}
        for i in range(len(all_ann)):
            all_fitnesses[i] = (all_cars[i][7] * total_dist + all_cars[i][4]) / all_cars[i][6]

        parent_1 = 0
        for i in all_fitnesses:
            if all_fitnesses[i] > all_fitnesses[parent_1]:
                parent_1 = i
        all_fitnesses.pop(parent_1)

        for i in all_fitnesses:
            parent_2 = i
            break
        for i in all_fitnesses:
            if all_fitnesses[i] > all_fitnesses[parent_2]:
                parent_2 = i

        new_orgs = []
        for i in range(orgs_per_gen):
            new_orgs.append(ga.mutate(ga.rep(all_ann[parent_1], all_ann[parent_2], average=True), mutation_rate))

        all_ann.clear()
        all_cars.clear()
        for i in range(orgs_per_gen):
            all_ann.append(new_orgs[i])
            all_cars.append([initial_pt, -math.pi / 2, vect.Vector(0, 0), temp_lst.copy(), 0, False, 0, 0])

        tm = 0
        gen += 1

    tm += 1
    pygame.display.update()
    # time.sleep(0.01)

pygame.quit()

print("weights:", all_ann[0].weights)
print("biases:", all_ann[0].biases)