import math, pygame, random, time
import import_ann as ann

pygame.init()

width = 800
height = 600
canvas = (width, height)
running = True
orgs_per_gen = 10
gens = 10
all_ann = []

scrn = pygame.display.set_mode(canvas)

def gameOver(a):
    if (a[0][0] == a[0][1] == a[0][2] == 1) or (a[1][0] == a[1][1] == a[1][2] == 1) or (a[2][0] == a[2][1] == a[2][2] == 1) or (a[0][0] == a[1][0] == a[2][0] == 1) or (a[0][1] == a[1][1] == a[2][1] == 1) or (a[0][2] == a[1][2] == a[2][2] == 1) or (a[0][0] == a[1][1] == a[2][2] == 1) or (a[0][2] == a[1][1] == a[2][0] == 1):
        return [True, 1]
    elif (a[0][0] == a[0][1] == a[0][2] == -1) or (a[1][0] == a[1][1] == a[1][2] == -1) or (a[2][0] == a[2][1] == a[2][2] == -1) or (a[0][0] == a[1][0] == a[2][0] == -1) or (a[0][1] == a[1][1] == a[2][1] == -1) or (a[0][2] == a[1][2] == a[2][2] == -1) or (a[0][0] == a[1][1] == a[2][2] == -1) or (a[0][2] == a[1][1] == a[2][0] == -1):
        return [True, 2]
    elif not(a[0][0] == 0 or a[0][1] == 0 or a[0][2] == 0 or a[1][0] == 0 or a[1][1] == 0 or a[1][2] == 0 or a[2][0] == 0 or a[2][1] == 0 or a[2][2] == 0):
        return [True, 0]
    return [False]

def matchBetween(a, b):
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    while not(gameOver(board)[0]):
        inputs = [x for x in board[0]]
        for i in range(1, 3):
            for j in range(3):
                inputs.append(board[i][j])
        a.feedForward(inputs)
        a_outputs_lst = a.activations[-1]
        a_outputs_dict = {}
        for i in range(len(a_outputs_lst)):
            a_outputs_dict[i] = a_outputs_lst[i]
        temp = 0
        for i in range(len(a_outputs_dict)):
            if a_outputs_dict[i] > a_outputs_dict[temp]:
                temp = i
        while board[temp // 3][temp % 3] != 0:
            a_outputs_dict.pop(temp)
            available = []
            for i in a_outputs_dict:
                available.append(i)
            temp = available[0]
            for i in available:
                if a_outputs_dict[i] > a_outputs_dict[temp]:
                    temp = i
        board[temp // 3][temp % 3] = 1
        win = gameOver(board)
        if win[0]:
            if win[1] == 1:
                return 1
            else:
                return 0

        temp_board = [[], [], []]
        for i in range(3):
            for j in range(3):
                temp_board[i].append(-board[i][j])
        inputs = [x for x in temp_board[0]]
        for i in range(1, 3):
            for j in range(3):
                inputs.append(temp_board[i][j])
        b.feedForward(inputs)
        b_outputs_lst = b.activations[-1]
        b_outputs_dict = {}
        for i in range(len(b_outputs_lst)):
            b_outputs_dict[i] = b_outputs_lst[i]
        temp = 0
        for i in range(len(b_outputs_dict)):
            if b_outputs_dict[i] > b_outputs_dict[temp]:
                temp = i
        while board[temp // 3][temp % 3] != 0:
            b_outputs_dict.pop(temp)
            available = []
            for i in b_outputs_dict:
                available.append(i)
            temp = available[0]
            for i in available:
                if b_outputs_dict[i] > b_outputs_dict[temp]:
                    temp = i
        board[temp // 3][temp % 3] = -1
    win = gameOver(board)
    if win[1] == 2:
        return -1
    else:
        return 0

def rep(a, b, average = False):
    new_org = ann.NeuralNetwork(a.all_neurons)
    if average:
        for i in range(len(a.weights)):
            for j in range(len(a.weights[i])):
                for k in range(len(a.weights[i][j])):
                    new_org.weights[i][j][k] = (a.weights[i][j][k] + b.weights[i][j][k]) / 2
        for i in range(len(a.biases)):
            for j in range(len(a.biases[i])):
                new_org.biases[i][j] = (a.biases[i][j] + b.biases[i][j]) / 2
    else:
        for i in range(len(a.weights)):
            for j in range(len(a.weights[i])):
                for k in range(len(a.weights[i][j])):
                    if random.choice([0, 1]):
                        new_org.weights[i][j][k] = a.weights[i][j][k]
                    else:
                        new_org.weights[i][j][k] = b.weights[i][j][k]
        for i in range(len(a.biases)):
            for j in range(len(a.biases[i])):
                if random.choice([0, 1]):
                    new_org.biases[i][j] = a.biases[i][j]
                else:
                    new_org.biases[i][j] = b.biases[i][j]
    return new_org

def mutate(a):
    pass

for i in range(orgs_per_gen):
    all_ann.append(ann.NeuralNetwork([9, 12, 12, 9]))

for g in range(gens):
    winners = []
    draws = []
    for i in range(int(len(all_ann) / 2)):
        result = matchBetween(all_ann[i], all_ann[int(i + len(all_ann) / 2)])
        if result == 1:
            winners.append(all_ann[i])
        elif result == -1:
            winners.append(all_ann[int(i + len(all_ann) / 2)])
        else:
            draws.append(all_ann[i])
            draws.append(all_ann[int(i + len(all_ann) / 2)])

    new_orgs = []
    if len(winners) > 1:
        for i in range(orgs_per_gen):
            org_1 = random.randrange(0, len(winners))
            org_2 = random.randrange(0, len(winners))
            while org_1 == org_2:
                org_2 = random.randrange(0, len(winners))
            new_orgs.append(rep(winners[org_1], winners[org_2]))
    elif len(winners):
        for i in range(orgs_per_gen):
            new_orgs.append(rep(winners[0], draws[random.randrange(0, len(draws))]))
    else:
        for i in range(orgs_per_gen):
            org_1 = random.randrange(0, len(draws))
            org_2 = random.randrange(0, len(draws))
            while org_1 == org_2:
                org_2 = random.randrange(0, len(draws))
            new_orgs.append(rep(draws[org_1], draws[org_2]))
    all_ann = new_orgs.copy()
    new_orgs.clear()
    time.sleep(1)

print(all_ann[0].weights)
print(all_ann[0].biases)

pygame.quit()

cpu = ann.NeuralNetwork(all_ann[0].all_neurons)
cpu.weights = all_ann[0].weights
cpu.biases = all_ann[0].biases

board = []
for i in range(9):
    board.append(0)
print()
print(board[:3])
print(board[3:6])
print(board[6:])
print()

while True:
    p1 = int(input("[0, 8]: "))
    while board[p1] != 0:
        p1 = int(input("[0, 8]: "))
    board[p1] = 1

    print()
    print(board[:3])
    print(board[3:6])
    print(board[6:])
    print()

    if ((board[0] == board[1] == board[2] == 1) or (board[3] == board[4] == board[5] == 1) or (board[6] == board[7] == board[8] == 1) or (board[0] == board[3] == board[6] == 1) or (board[1] == board[4] == board[7] == 1) or (board[2] == board[5] == board[8] == 1) or (board[0] == board[4] == board[8] == 1) or (board[2] == board[4] == board[6] == 1)):
        print("You won!")
        break
    elif not(board[0] == 0 or board[1] == 0 or board[2] == 0 or board[3] == 0 or board[4] == 0 or board[5] == 0 or board[6] == 0 or board[7] == 0 or board[8] == 0):
        print("Draw!")
        break

    temp_board = []
    for i in board:
        temp_board.append(-i)
    cpu.feedForward(temp_board)
    outputs_lst = cpu.activations[-1]
    outputs_dict = {}
    for i in range(len(outputs_lst)):
        outputs_dict[i] = outputs_lst[i]
    temp = 0
    for i in range(len(outputs_dict)):
        if outputs_dict[i] > outputs_dict[temp]:
            temp = i
    while board[temp] != 0:
        outputs_dict.pop(temp)
        available = []
        for i in outputs_dict:
            available.append(i)
        temp = available[0]
        for i in available:
            if outputs_dict[i] > outputs_dict[temp]:
                temp = i
    board[temp] = -1

    print(board[:3])
    print(board[3:6])
    print(board[6:])
    print()

    if ((board[0] == board[1] == board[2] == -1) or (board[3] == board[4] == board[5] == -1) or (board[6] == board[7] == board[8] == -1) or (board[0] == board[3] == board[6] == -1) or (board[1] == board[4] == board[7] == -1) or (board[2] == board[5] == board[8] == -1) or (board[0] == board[4] == board[8] == -1) or (board[2] == board[4] == board[6] == -1)):
        print("CPU won!")
        break