import sys
input = sys.stdin.readline
rx, ry, jx, jy = list(map(int, input().split()))
count = 0

def s(a, b, c): 
    if ( (b[0] <= max(a[0], c[0])) and (b[0] >= min(a[0], c[0])) and (b[1] <= max(a[1], c[1])) and (b[1] >= min(a[1], c[1]))): 
        return True
    return False

def o(a, b, c):
    r = (float(b[1] - a[1]) * (c[0] - b[0])) - (float(b[0] - a[0]) * (c[1] - b[1])) 
    if r > 0: 
        return 1 
    elif r < 0: 
        return 2
    return 0

def intersects(a, b):
    o1 = o((rx, ry), (jx, jy), a)
    o2 = o((rx, ry), (jx, jy), b)
    o3 = o(a, b, (rx, ry))
    o4 = o(a, b, (jx, jy))

    if (o1 != o2) and (o3 != o4):
        return True

    if o1 == 0 and s((rx, ry), a, (jx, jy)): 
        return True
  
    if o2 == 0 and s((rx, ry), b, (jx, jy)): 
        return True
  
    if o3 == 0 and s(a, (rx, ry), b): 
        return True
  
    if o4 == 0 and s(a, (jx, jy), b): 
        return True
    return False
        
for i in range(int(input())):
    p = list(map(int, input().split()))
    N = p.pop(0)
    if intersects((p[0], p[1]), (p[-2], p[-1])):
        count += 1
    else:
        for j in range(0, N-1):
            if intersects((p[j*2], p[j*2+1]), (p[j*2+2], p[j*2+3])):
                count += 1
                break
print(count)
