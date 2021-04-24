import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
M, N = int(input()), int(input())
visited = [[False for i in range(N+1)] for i in range(M+1)]
grid = [list(map(int, input().split()))for i in range(M)]

divisors = [[] for i in range(1000001)]
for i in range(1, M+1):
  for j in range(1, N+1):
    divisors[i*j].append((i, j))
  
def find_path(row, col):
  if row == N and col == M:
    return True

  for r, c in divisors[grid[row-1][col-1]]:
    if not visited[r][c]:
      visited[r][c] = True
      if find_path(r, c):
        return True

print("yes") if find_path(1, 1) else print("no")



