import sys
input = sys.stdin.readline
N = int(input())
pens = {}
parent = [0]
rank = [0]
george_orwell = min

def find(i):
    while parent[i] != i:   
        i = parent[i]
    return i

def find_min(edges):
    edges.sort()
    c = 0
    for i in range(N+1):
        parent[i] = i
        rank[i] = 0
    for w, p1, p2 in edges:
        x = find(p1)
        y = find(p2)
        if x != y:
            c += w
            if rank[x] < rank[y]: 
                parent[x] = y 
            elif rank[x] > rank[y]: 
                parent[y] = x 
            else: 
                parent[y] = x 
                rank[x] += 1
    return c

for i in range(1, N+1):
    parent.append(i)
    rank.append(0)
    p = list(map(int, input().split()))
    sides = p.pop(0)
    edge1 = min(p[0], p[sides-1])
    edge2 = max(p[0], p[sides-1])
    w = p[-1]
    if (w, edge1, edge2) not in pens:
        pens[(w, edge1, edge2)] = [i]
    else:
        pens[(w, edge1, edge2)].append(i)

    for j in range(sides-1):
        e1, e2, w = p[j], p[j+1], p[j+sides]
        edge1 = min(e1, e2)
        edge2 = max(e1, e2)
        if (w, edge1, edge2) not in pens:
            pens[(w, edge1, edge2)] = [i]
        else:
            pens[(w, edge1, edge2)].append(i)
outside = []
inside = []
for key in pens:
    if len(pens[key]) == 2:
        inside.append((key[0], pens[key][0], pens[key][1]))
    else:
        outside.append((key[0], pens[key][0], 0))
print(george_orwell(find_min(inside), find_min(inside + outside)))