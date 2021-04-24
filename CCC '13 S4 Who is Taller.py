import sys
import heapq

input = sys.stdin.readline

N, M = list(map(int, input().split()))
d = [[] for i in range(N+1)]
for i in range(M):
    a, b = list(map(int, input().split()))
    d[a].append(b)
    
start, end = list(map(int, input().split()))

visited_x = [False] * (N+1)
visited_y = [False] * (N+1)

queue_x = [[len(d[start]), start]]
queue_y = [[len(d[end]), end]]

taller = None

if d[start] == []:
  queue_x = []
if d[end] == []:
  queue_y = []

while queue_x or queue_y:
    x, y = [0, 0]
    if queue_x:
        lx, x = heapq.heappop(queue_x)
        visited_x[x] = True
    if queue_y:
        ly, y = heapq.heappop(queue_y)
        visited_y[y] = True

    if x == end:
        taller = True
        break

    if y == start:
        taller = False
        break
    if x != 0:
        for f in d[x]:
          if not visited_x[f]:
            heapq.heappush(queue_x, [len(d[f]), f])
    if y != 0:
        for f in d[y]:
          if not visited_y[f]:
            heapq.heappush(queue_y, [len(d[f]), f])

if taller is None:
    print("unknown")

else:
    print("yes") if taller else print("no")
#print(d)