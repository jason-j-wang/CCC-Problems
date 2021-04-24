import sys
input = sys.stdin.readline

goal = int(input())
clubs = [int(input()) for i in range(int(input()))]
clubs.sort(reverse=True)
memo = {}
strokes = 0
def find_strokes(dist_left):
    global strokes
    if dist_left == 0:
        return True

    if dist_left < 0:
        return False

    if memo.get(dist_left) != None:
        return memo[dist_left]

    for club in clubs:
        memo[dist_left - club] = find_strokes(dist_left - club)
        if memo[dist_left - club]:
            strokes += 1
            return True
            
    return False
  
if find_strokes(goal):
    print("Roberta wins in", strokes, "strokes.")
else:
    print("Roberta acknowledges defeat.")