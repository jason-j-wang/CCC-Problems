import sys
input = sys.stdin.readline
reactions = {"AABDD": [-2, -1, 0, -2], "ABCD": [-1, -1, -1, -1], "CCD": [0, 0, -2, -1], "BBB": [0, -3, 0, 0], "AD": [-1, 0, 0, -1]}
memo = {}
#turn == True when it is patrick's turn
def find_winner(particles, turn, first_step=False):
    if particles == [0, 0, 0, 0]:
        return True if not turn else False
    
    if (particles[0], particles[1], particles[2], particles[3], turn) in memo:
        return memo[(particles[0], particles[1], particles[2], particles[3], turn)]

    if (particles[0], particles[1], particles[2], particles[3], not turn) in memo:
        return not memo[(particles[0], particles[1], particles[2], particles[3], not turn)]

    total = []
    for r in reactions:
        neg = False
        A = reactions[r][0] + particles[0]
        B = reactions[r][1] + particles[1]
        C = reactions[r][2] + particles[2]
        D = reactions[r][3] + particles[3]
        if min(A, B, C, D) < 0:
            neg = True
        if not neg:
            total.append(find_winner([A, B, C, D], not turn))
            if turn and any(total):
                memo[(particles[0], particles[1], particles[2], particles[3], turn)] = True
                return True

    if total:
        memo[(particles[0], particles[1], particles[2], particles[3], turn)] = any(total) if turn else all(total)
        return any(total) if turn else all(total)
    else:
        memo[(particles[0], particles[1], particles[2], particles[3], turn)] = True if not turn else False
        return True if not turn else False

for i in range(int(input())):
    particles = list(map(int, input().split()))
    print("Patrick") if find_winner(particles, True, True) else print("Roland")