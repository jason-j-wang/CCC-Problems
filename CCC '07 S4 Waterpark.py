import sys
input = sys.stdin.readline
N = int(input())
slides = [[] for i in range(N+1)]
memo = {}

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    slides[a].append(b)

def find_path(node):
    if node == N:
        return 1

    if node in memo:
        return memo[node]

    total = [find_path(next) for next in slides[node]]
    memo[node] = sum(total)
    return sum(total)

print(find_path(1))   