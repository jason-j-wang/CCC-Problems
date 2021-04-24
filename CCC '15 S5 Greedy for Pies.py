import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
#TLEs / MLEs
N = int(input())
npie = [int(input()) for _ in range(N)]
M = int(input())

mpie = [int(input()) for _ in range(M)]
mpie.sort()

memo = [[[[-1 for _ in range(M+1)] for _ in range(M+1)] for _ in range(2)] for _ in range(N+1)]

def get_pies(pos, can_take, left, right):

    if memo[pos][can_take][left][right] != -1:
        return memo[pos][can_take][left][right]
    if pos == N:
        if left <= right:
            if can_take:
                memo[pos][can_take][left][right] = mpie[right] + get_pies(pos, False, left, right-1)
                return memo[pos][can_take][left][right]
            memo[pos][can_take][left][right] = get_pies(pos, True, left+1, right)
            return memo[pos][can_take][left][right]
        return 0

    if can_take:
        without_M = max((npie[pos] + get_pies(pos+1, False, left, right)), get_pies(pos+1, True, left, right))
        with_M = get_pies(pos, False, left, right-1) + mpie[right] if left <= right else 0
        memo[pos][can_take][left][right] = max(with_M, without_M)
        return memo[pos][can_take][left][right]

    else:
        with_M = get_pies(pos, True, left+1, right) if left <= right else 0
        memo[pos][can_take][left][right] = max(with_M, get_pies(pos+1, True, left, right))
        return memo[pos][can_take][left][right]
print(get_pies(0, True, 0, M-1))