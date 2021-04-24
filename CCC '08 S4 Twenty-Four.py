import sys
from itertools import permutations
input = sys.stdin.readline

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0 or (a / b) % 1 != 0:
        return -6969
    return a//b

functions = [add, sub, mul, div]

def special(perm, highest):
    a, b, c, d = perm
    for first in functions:
        for second in functions:
            for third in functions:
                final = third(first(a, b), second(c, d))
                if final == 24:
                    return 24
                elif final < 24 and final > highest:
                    highest = final
    return highest


def do(cards):
    highest = 0
    for perm in permutations(cards):
        a, b, c, d = perm

        for first in functions:
            for second in functions:
                for third in functions:
                    ans = third(second(first(a, b), c), d)
                    if ans == 24:
                        return 24
                    elif ans < 24 and ans > highest:
                        highest = ans
        highest = special(perm, highest)
    return highest
for i in range(int(input())):
    cards = [int(input()), int(input()), int(input()), int(input())]
    print(do(cards))