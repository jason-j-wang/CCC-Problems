import sys
input = sys.stdin.readline
row, col = list(map(int, input().split()))
cats = [list(map(int, input().split())) for i in range(int(input()))]
count = 0

memo = {}
memo[(0, 0)] = 1            

def count_paths(pos):
    if (pos[0], pos[1]) not in memo:
        if [pos[0]+1, pos[1]+1] in cats:
            memo[(pos[0], pos[1])] = 0
        else:
            if pos[0] > 0 and pos[1] > 0:
                memo[(pos[0], pos[1])] = memo[(pos[0]-1, pos[1])] + memo[(pos[0], pos[1] - 1)]
            else:
                memo[(pos[0], pos[1])] = memo[(pos[0], pos[1] - 1)] if pos[0] == 0 else memo[(pos[0]-1, pos[1])]

for i in range(row):
    for j in range(col):
        count_paths([i, j])

print(memo[(row-1, col-1)])
