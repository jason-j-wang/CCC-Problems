import heapq, sys
input = sys.stdin.readline

K, N, M = list(map(int, input().split()))
adj = [[] for i in range(N+1)]
for i in range(M):
    a, b, t, h = list(map(int, input().split()))
    adj[a].append([t, h, b])
    adj[b].append([t, h, a])

start, end = list(map(int, input().split()))
def find_path(start, end): 
    islands = [0 for i in range(N+1)]
    q = [[0, K, start]]
    while q:
        t, h, index = heapq.heappop(q)
        if index == end:
            return t
        islands[index] = h
        for time, hull, dest in adj[index]:     
            new_time = t + time
            new_hull = h - hull    
            if new_hull> islands[dest]:
                heapq.heappush(q, [new_time, new_hull, dest])

    return -1

print(find_path(start, end))