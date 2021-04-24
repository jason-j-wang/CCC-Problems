import sys
input = sys.stdin.readline

friends = {}

wait_time = 1

for _ in range(int(input())):
    entry, friend = [i for i in input().split()]
    friend = int(friend)

    if entry == "R":
        for f in friends:
            if not friends[f][0]:
                friends[f][1] += wait_time
        if friends.get(friend) == None:
            friends[friend] = [False, 0]
        else:
            friends[friend][0] = False
        wait_time = 1
    elif entry == "S":
        for f in friends:
            if not friends[f][0]:
                friends[f][1] += wait_time
        friends[friend][0] = True
        wait_time = 1

    else:
        wait_time = friend

lst = []
for friend in friends:
    time = -1
    if friends[friend][0] == True:
        time = friends[friend][1]
    lst.append((friend, time))
lst.sort()

for f in lst:
    print(f[0], f[1])