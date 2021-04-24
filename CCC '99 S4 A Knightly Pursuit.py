import sys
input = sys.stdin.readline
moves = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]

def add_paths(r, c):
    for move in moves:
 
        nr = r + move[0]
        nc = c + move[1]
       
        if (nr > 0 and nr < row +1 and nc > 0 and nc < col + 1) and not visited[nr][nc]:
            visited[nr][nc] = True
            next_queue.append((nr, nc))

for _ in range(int(input())):
    row, col = int(input()), int(input())
    pr, pc = int(input()), int(input())
    kr, kc = int(input()), int(input())
    board = [[999 for _ in range(col+1)] for _ in range(row+1)]
    visited = [[False for _ in range(col+1)] for _ in range(row+1)]
    queue = [(kr, kc)]
    board[kr][kc] = 0
    next_queue = []
    steps = 0
    while queue:
       # print(queue, next_queue)
        r, c = queue.pop(0)
        visited[r][c] = True
        board[r][c] = steps
        add_paths(r, c)
        if not queue:
            queue = next_queue
            next_queue = []
            steps += 1
    m = 0
    
    win = False
    for pm in range(pr, row):
        if board[pm][pc] == m:
            win = True
            print("Win in", m, "knight move(s).")
            break
        elif board[pm][pc] < m and m%2 == board[pm][pc] %2:
            win = True
            print("Win in", m, "knight move(s).")
            break
        elif board[pm+1][pc] == m:
            break
        m += 1
    m= 0
    if not win:
        for pm in range(pr, row+1):
            if pm < row:
                if board[pm+1][pc] == m:
                    print("Stalemate in", m, "knight move(s).")
                    break
                elif board[pm][pc] < m and m%2 != board[pm][pc]%2:
                    print("Stalemate in", m+1, "knight move(s).")
                    break
            elif pm == row:
                print("Loss in", m-1, "knight move(s).")
            m+= 1