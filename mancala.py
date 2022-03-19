board = [0, [4, 4, 4, 4, 4, 4, 0], [4, 4, 4, 4, 4, 4, 0]]

turn = 1
move = 7
air = 0

def ask():
    global move, air, board

    move = int(input("Player " + str(int((3 - turn) / 2)) + ": "))
    while board[turn][move - 1] == 0:
        move = int(input("Player " + str(int((3 - turn) / 2)) + ": "))

    air = board[turn][move - 1]
    board[turn][move - 1] = 0

def showBoard():
    temp = []
    for i in range(5, -1, -1):
        temp.append(board[-1][i])
    print(board[-1][-1], temp)
    print(board[1][:6], board[1][-1], '\n')

def sameSide():
    global air, turn, move, board

    while air > 0 and move < 7:
        board[turn][move] += 1
        air -= 1
        move += 1
        showBoard()

    if air == 0 and move != 7:
        # capture
        if board[turn][move - 1] == 1 and board[-turn][6 - move] != 0:
            board[turn][6] += board[turn][move - 1] + board[-turn][6 - move]
            board[turn][move - 1] = 0
            board[-turn][6 - move] = 0
            showBoard()
        turn *= -1
    elif air != 0 and move == 7:
        move = 0
        oppSide()

def oppSide():
    global air, turn, move, board

    while air > 0 and move < 6:
        board[-turn][move] += 1
        air -= 1
        move += 1
        showBoard()

    if air == 0:
        turn *= -1
    elif air != 0 and move == 6:
        move = 0
        sameSide()

def gameOver():
    c = 0
    for i in range(6):
        if board[1][i] == 0:
            c += 1
        else:
            break
    if c == 6:
        return True
    else:
        c = 0
        for i in range(6):
            if board[-1][i] == 0:
                c += 1
            else:
                break
    if c == 6:
        return True
    else:
        return False

showBoard()
while not(gameOver()):
    ask()
    sameSide()

for i in range(6):
    while board[1][i] > 0:
        board[1][i] -= 1
        board[1][6] += 1
    while board[-1][i] > 0:
        board[-1][i] -= 1
        board[-1][6] += 1
    showBoard()

if board[1][-1] > board[-1][-1]:
    print("Player 1 Wins!")
elif board[1][-1] < board[-1][-1]:
    print("Player 2 Wins!")
else:
    print("Tie!")