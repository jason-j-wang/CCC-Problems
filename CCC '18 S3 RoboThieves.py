import sys

input = sys.stdin.readline

dimensions = list(map(int, input().split()))
row = dimensions[0]
col = dimensions[1]

camera = False
impossible = False
start = []
conveyors = ["L", "R", "U", "D"]
directions = {"L": [0, -1], "R": [0, 1], "U": [-1, 0], "D": [1, 0]}
end_points = {}

cameras = []

#factory = [[cell for cell in input()] for i in range(row)]
factory = []
traversed = []

for i in range(row):
    r = []
    tr = []
    line = input()
    for j in range(col):
        r.append(line[j])
        tr.append(-1)
        if line[j] == "C":
            camera = True
            cameras.append([i, j])
        elif line[j] == "S":
            start = [i, j]
       
    factory.append(r)
    traversed.append(tr)

if camera:
    for a in range(len(cameras)):
        i , j = cameras[a]
    
        #NSEW
        for k in range(i, -1, -1):
            if factory[k][j] == ".":
                factory[k][j] = "N"
            elif factory[k][j] == "W":
                break
            elif factory[k][j] == "S":
                impossible = True
                break

        for l in range(i, row):
            if factory[l][j] == ".":
                factory[l][j] = "N"
            elif factory[l][j] == "W":
                break
            elif factory[l][j] == "S":
                impossible = True
                break

        for m in range(j, col):
            if factory[i][m] == ".":
                factory[i][m] = "N"
            elif factory[i][m] == "W":
                break
            elif factory[i][m] == "S":
                impossible = True
                break

        for n in range(j, -1, -1):
            if factory[i][n] == ".":
                factory[i][n] = "N"
            elif factory[i][n] == "W":
                break
            elif factory[i][n] == "S":
                impossible = True
                break

for i in range(row):
    for j in range(col):
        if factory[i][j] in conveyors:
            
            passed = []
            x, y = i, j
            while factory[x][y] in conveyors:
                if [x, y] not in passed:
                    passed.append([x, y])
                    temp = x
                    x += directions[factory[x][y]][0]
                    y += directions[factory[temp][y]][1]
                elif [x, y] in passed:
                    factory[x][y] = "W"
                    break

            
            end_points[(i, j)] = [x, y]
            
#print(end_points)                  

def find_path(pos):
    
    if factory[pos[0]][pos[1]] == 'W' or factory[pos[0]][pos[1]] == "N":
        return 
    if visited[pos[0]][pos[1]]:
        return

    visited[pos[0]][pos[1]] = True
    
    x, y = pos
    if factory[x][y] == '.' or factory[x][y] == "S":

        next_queue.append([x+1, y])
        next_queue.append([x-1, y])
        next_queue.append([x, y+1])
        next_queue.append([x, y-1])

if not impossible:
    visited = [[False for i in range(col)] for i in range(row)]
    steps = 0
    queue = [start]
    next_queue = []

    while queue:
        r, c = queue.pop(0)
        #print(queue, next_queue)
        
        if factory[r][c] in conveyors:
            r, c = end_points[(r, c)]

        if factory[r][c] == ".":
            if traversed[r][c] == -1:
                traversed[r][c] = steps
            elif traversed[r][c] > steps:
                traversed[r][c] = steps

        #print(r, c)
        find_path([r, c])

        if not queue:
            queue = next_queue
            next_queue = []
            steps += 1
#print(traversed)
for i in range(row):
    for j in range(col):
        if factory[i][j] == "." or factory[i][j] == "N":
            print(traversed[i][j])

