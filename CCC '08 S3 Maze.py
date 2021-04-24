import sys
input = sys.stdin.readline

def find_path(pos):
    global next_queue
    if visited[pos[0]][pos[1]] or city[pos[0]][pos[1]] == '*':
        return 
    visited[pos[0]][pos[1]] = True

    if city[pos[0]][pos[1]] == '+':
        if pos[0] -1 != -1:
            queue.append([pos[0] - 1, pos[1]])
            next_queue.append(1)
        if pos[0] + 1 != r:
            queue.append([pos[0] +1, pos[1]])
            next_queue.append(1)
        if pos[1] -1 != -1:
            queue.append([pos[0], pos[1] -1])
            next_queue.append(1)
        if pos[1] + 1 != c:
            queue.append([pos[0], pos[1] + 1])
            next_queue.append(1)

    elif city[pos[0]][pos[1]] == '-':
        if pos[1] -1 != -1:
            queue.append([pos[0], pos[1] -1])
            next_queue.append(1)
        if pos[1] + 1 != c:
            queue.append([pos[0], pos[1] + 1])
            next_queue.append(1)
    
    elif city[pos[0]][pos[1]] == '|':
        if pos[0] -1 != -1:
            queue.append([pos[0] - 1, pos[1]])
            next_queue.append(1)
        if pos[0] + 1 != r:
            queue.append([pos[0] +1, pos[1]])
            next_queue.append(1)

    else:
        return


for i in range(int(input())):
    r, c = int(input()), int(input())
    city = []

    for i in range(r):
        temp = str(input())
        row = []
        for j in range(c):
            row.append(temp[j])
        city.append(row) 

    visited = [[False for i in range(c)] for i in range(r)]

    count = 1
    queue = [[0, 0]]
    queued = 1
    finished = False
    next_queue = []

    while queue:
        row, col = queue.pop(0)
        if row == r-1 and col == c-1:
            if city[row][col] != '*':
                finished = True
                break
        
        find_path([row, col])
        queued -= 1
        if queued == 0:
            queued = len(next_queue)
            next_queue = []
            count += 1

    if finished:
        print(count)
    else:
        print(-1)