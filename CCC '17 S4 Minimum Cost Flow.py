import sys
input = sys.stdin.readline

B, P, D = map(int, input().split())
pipes = []

parent = []
rank = []
for i in range(B+1):
    parent.append(i)
    rank.append(0)
def find(i):
    while parent[i] != i:
        i = parent[i]
    return i
    
def find_min(pipes):
    days = 0

    for w, not_active, b1, b2 in pipes:

        x = find(b1)
        y = find(b2)
        
        if x != y:
            maxw = w
            last_pipe = not_active
            if rank[x] < rank[y]: 
                parent[x] = y 
            elif rank[x] > rank[y]: 
                parent[y] = x 
            else: 
                parent[y] = x 
                rank[x] += 1

            if not_active:
                days += 1

    if last_pipe:
        for i in range(B+1):
            parent[i] = i
            rank[i] = 0
        for w, not_active, b1, b2 in pipes:
            x = find(b1)
            y = find(b2)
            
            if x != y:
                if w < maxw or (w == maxw and not not_active):
                    if rank[x] < rank[y]: 
                        parent[x] = y 
                    elif rank[x] > rank[y]: 
                        parent[y] = x 
                    else: 
                        parent[y] = x 
                        rank[x] += 1
                elif not not_active and w <= D:
                    return days-1

       
    return days


for i in range(P):
    b1, b2, w = map(int, input().split())
    active = False if i < B -1 else True #False = originally in use
    pipes.append((w, active, b1, b2))

pipes.sort()
print(find_min(pipes))



