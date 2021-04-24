import sys
input = sys.stdin.readline
for i in range(int(input())):
    highest = 0
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    if X[-1] > Y[0]:
        print("The maximum distance is 0")
    else:
        for j in range(len(X)):
            for k in range(j, len(X)):
                if Y[k] >= X[j]:
                    if k - j > highest:
                        highest = k-j
        print("The maximum distance is", highest)
