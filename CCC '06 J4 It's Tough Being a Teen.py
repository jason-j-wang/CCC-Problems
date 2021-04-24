import sys
input = sys.stdin.readline

tasks = [1, 2, 3, 4, 5, 6, 7]
completed = [False] * 8
completed[0] = True

p = [[] for _ in range(8)]

p[7].append(1)
p[4].append(1)
p[1].append(2)
p[4].append(3)
p[5].append(3)

while True:
    b, a = int(input()), int(input())
    if b == 0 and a == 0:
        break
    p[a].append(b)

order = []
for i in range(7):
    for task in tasks:
        if not completed[task] and all(completed[t] for t in p[task]):
            completed[task] = True
            order.append(task)
            break

print("Cannot complete these tasks. Going to bed.") if len(order) < 7 else print(" ".join(str(t) for t in order))
