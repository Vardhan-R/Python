from built_modules import import_ann as ann, import_geneticalgorithm as ga
from copy import deepcopy
import collections, manim, numpy as np, pygame

# pygame.init()

# width = 1600
# height = 1200
# canvas = (width, height)
# running = True
orgs_per_gen = 6
gens = 90

# scrn = pygame.display.set_mode(canvas)

def gameOver(arr: np.ndarray):
    for i in range(3):
        row = dict(collections.Counter(arr[i])) # {1: 2, 0: 1}
        try:
            player_1_cnt = row[1]
        except:
            player_1_cnt = 0
        try:
            player_2_cnt = row[-1]
        except:
            player_2_cnt = 0

        if player_1_cnt == 3:
            return (True, 1)
        elif player_2_cnt == 3:
            return (True, 2)

        col = dict(collections.Counter(arr[:, i])) # {0: 1, -1: 2}
        try:
            player_1_cnt = col[1]
        except:
            player_1_cnt = 0
        try:
            player_2_cnt = col[-1]
        except:
            player_2_cnt = 0

        if player_1_cnt == 3:
            return (True, 1)
        elif player_2_cnt == 3:
            return (True, 2)

    diag_1 = dict(collections.Counter(arr.diagonal()))
    try:
        player_1_cnt = diag_1[1]
    except:
        player_1_cnt = 0
    try:
        player_2_cnt = diag_1[-1]
    except:
        player_2_cnt = 0

    if player_1_cnt == 3:
        return (True, 1)
    elif player_2_cnt == 3:
        return (True, 2)

    diag_2 = dict(collections.Counter(np.fliplr(arr).diagonal()))
    try:
        player_1_cnt = diag_2[1]
    except:
        player_1_cnt = 0
    try:
        player_2_cnt = diag_2[-1]
    except:
        player_2_cnt = 0

    if player_1_cnt == 3:
        return (True, 1)
    elif player_2_cnt == 3:
        return (True, 2)

    if np.count_nonzero(arr) == 9:
        return (True, None)

    return False

def matchBetween(org_1: ann.NeuralNetwork, org_2: ann.NeuralNetwork) -> int:
    orgs = [org_1, org_2]
    board_arr = np.zeros((3, 3))
    while True:
        for i in range(2):
            board_flattened_lst = list(np.reshape(board_arr, 9))
            orgs[i].feedForward(board_flattened_lst)
            all_pos_activations = orgs[i].activations[-1]
            while True:
                pos = np.argmax(np.array(all_pos_activations))
                if board_flattened_lst[pos]:
                    all_pos_activations[pos] = 0
                else:
                    board_flattened_lst[pos] = 1
                    break
            board_arr = -np.reshape(np.array(board_flattened_lst), (3, 3)) # (the minus sign makes all the 1's -1's and vice versa)
            game_over_state = gameOver((2 * i - 1) * board_arr) # 0 ==> -1, 1 ==> 1 (the multiplication ensures that the board is in player 1's point of view)
            if game_over_state:
                return game_over_state[1]

def playAllMatches(all_orgs, orgs_per_gen):
    scores = np.zeros(orgs_per_gen)
    for i in range(orgs_per_gen - 1):
        for j in range(i + 1, orgs_per_gen):
            winner = matchBetween(all_orgs[i], all_orgs[j])
            if winner:
                scores[i] += 3 - 2 * winner # 1 ==> 1; 2 ==> -1
                scores[j] += 2 * winner - 3 # 1 ==> -1; 2 ==> 1
    return scores

def playMatch(org: ann.NeuralNetwork, human_start = True):
    board_arr = np.zeros((3, 3))
    if human_start:
        while True:
            print(board_arr)
            board_flattened_lst = list(np.reshape(board_arr, 9))
            board_flattened_lst[int(input("Position (0 to 8): "))] = -1
            board_arr = np.reshape(np.array(board_flattened_lst), (3, 3))
            print(board_arr)
            game_over_state = gameOver(board_arr)
            if game_over_state:
                if game_over_state[1] == 1:
                    print("CPU won!")
                elif game_over_state[1] == 2:
                    print("You won!")
                else:
                    print("Tie!")
                break
            org.feedForward(board_flattened_lst)
            all_pos_activations = org.activations[-1]
            while True:
                pos = np.argmax(np.array(all_pos_activations))
                if board_flattened_lst[pos]:
                    all_pos_activations[pos] = 0
                else:
                    board_flattened_lst[pos] = 1
                    break
            board_arr = np.reshape(np.array(board_flattened_lst), (3, 3))
            game_over_state = gameOver(board_arr)
            if game_over_state:
                print(board_arr)
                if game_over_state[1] == 1:
                    print("CPU won!")
                elif game_over_state[1] == 2:
                    print("You won!")
                else:
                    print("Tie!")
                break
    else:
        while True:
            print(board_arr)
            board_flattened_lst = list(np.reshape(board_arr, 9))
            org.feedForward(board_flattened_lst)
            all_pos_activations = org.activations[-1]
            while True:
                pos = np.argmax(np.array(all_pos_activations))
                if board_flattened_lst[pos]:
                    all_pos_activations[pos] = 0
                else:
                    board_flattened_lst[pos] = 1
                    break
            board_arr = np.reshape(np.array(board_flattened_lst), (3, 3))
            print(board_arr)
            game_over_state = gameOver(board_arr)
            if game_over_state:
                if game_over_state[1] == 1:
                    print("CPU won!")
                elif game_over_state[1] == 2:
                    print("You won!")
                else:
                    print("Tie!")
                break
            board_flattened_lst[int(input("Position (0 to 8): "))] = -1
            board_arr = np.reshape(np.array(board_flattened_lst), (3, 3))
            game_over_state = gameOver(board_arr)
            if game_over_state:
                print(board_arr)
                if game_over_state[1] == 1:
                    print("CPU won!")
                elif game_over_state[1] == 2:
                    print("You won!")
                else:
                    print("Tie!")
                break

def pickTopTwo(all_orgs: list[ann.NeuralNetwork], all_scores: list[float | int]):
    temp = np.argmax(all_scores)
    best_org_1 = all_orgs[temp]
    all_scores[temp] = -orgs_per_gen
    best_org_2 = all_orgs[np.argmax(all_scores)]
    return (best_org_1, best_org_2)

# all_orgs = [ann.NeuralNetwork((9, 6, 9)) for _ in range(orgs_per_gen)]
temp_org = ann.NeuralNetwork((9, 6, 9))
temp_org.loadNeuralNetwork("python_files/all_ann/tic_tc_toe_ai_gen_10")
for i in range(10):
    playMatch(temp_org)
# all_orgs = [ga.mutate(temp_org, 0.06) for _ in range(orgs_per_gen)]

# for i in range(gens - 1):
#     all_scores = playAllMatches(all_orgs, orgs_per_gen)
#     print(all_scores)

#     best_org_1, best_org_2 = pickTopTwo(all_orgs, all_scores)

#     temp_org = ga.rep(best_org_1, best_org_2, True)
#     all_orgs = [ga.mutate(temp_org, 0.06) for _ in range(orgs_per_gen)]

# best_org_1.saveNeuralNetwork("python_files/all_ann/tic_tc_toe_ai_gen_100")