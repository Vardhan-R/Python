board = [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

found_words = []
m = len(board)
n = len(board[0])
global_visited = []
temp_lst = []
for i in range(n):
    temp_lst.append(False)
for i in range(m):
    global_visited.append(temp_lst.copy())

def findWords(board, row, col, target_word, current_word="", visited=global_visited.copy()):
    new_current_word = current_word + board[row][col]
    if new_current_word == target_word:
        return True
    elif board[row][col] == target_word[len(current_word)]:
        new_visited = visited.copy()
        new_visited[row][col] = True
        if row < m - 1:
            if not(visited[row + 1][col]):
                found = findWords(board, row + 1, col, target_word, new_current_word, new_visited.copy())
                if found == True:
                    return found
        if col < n - 1:
            if not(visited[row][col + 1]):
                found = findWords(board, row, col + 1, target_word, new_current_word, new_visited.copy())
                if found == True:
                    return found
        if row > 0:
            if not(visited[row - 1][col]):
                found = findWords(board, row - 1, col, target_word, new_current_word, new_visited.copy())
                if found:
                    return found
        if col > 0:
            if not(visited[row][col - 1]):
                found = findWords(board, row, col - 1, target_word, new_current_word, new_visited.copy())
                if found:
                    return found
    return False

for i in words:
    b = False
    for j in range(m):
        for k in range(n):
            global_visited[j][k] = False
    for j in range(m):
        for k in range(n):
            if findWords(board, j, k, i):
                if i not in found_words:
                    found_words.append(i)
                b = True
                break
        if b:
            break
print(found_words)
