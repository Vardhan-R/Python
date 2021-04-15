board = []
for i in range(9):
    board.append(" ")

while True:
    print(board[:3])
    print(board[3:6])
    print(board[6:])
    p1 = int(input("X: "))
    while board[p1] != " ":
        p1 = int(input("X: "))
    board[p1] = "X"

    if ((board[0] == board[1] == board[2] == "X") or (board[3] == board[4] == board[5] == "X") or (board[6] == board[7] == board[8] == "X") or (board[0] == board[3] == board[6] == "X") or (board[1] == board[4] == board[7] == "X") or (board[2] == board[5] == board[8] == "X") or (board[0] == board[4] == board[8] == "X") or (board[2] == board[4] == board[6] == "X")):
        board[p1] = "X"
        print(board[:3])
        print(board[3:6])
        print(board[6:])
        print("X won!")
        break

    print(board[:3])
    print(board[3:6])
    print(board[6:])
    p2 = int(input("O: "))
    while board[p2] != " ":
        p2 = int(input("O: "))
    board[p2] = "O"

    if ((board[0] == board[1] == board[2] == "O") or (board[3] == board[4] == board[5] == "O") or (board[6] == board[7] == board[8] == "O") or (board[0] == board[3] == board[6] == "O") or (board[1] == board[4] == board[7] == "O") or (board[2] == board[5] == board[8] == "O") or (board[0] == board[4] == board[8] == "O") or (board[2] == board[4] == board[6] == "O")):
        board[p1] = "X"
        print(board[:3])
        print(board[3:6])
        print(board[6:])
        print("O won!")
        break