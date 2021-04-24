import sys
input = sys.stdin.readline
C, R, D = map(int, input().split())
roads = []
dest = set()

def find_weight():

    for w, c1, c2 in roads:
        try:
            dest.remove(c1)
        except:
            pass
        try:
            dest.remove(c2)
        except:
            pass

        if not dest:
            maxw = w
            return maxw
    
for _ in range(R):
    c1, c2, w = map(int, input().split())
    roads.append((w, c1, c2))
roads.sort(reverse=True)
dest.add(1)
for _ in range(D):
    dest.add(int(input()))

print(find_weight())