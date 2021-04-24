friends = {}
for i in range(int(input())):
    temp = list(input().split())
    if len(temp) == 2:
        friends[temp[0]] = temp[1]

        if friends.get(temp[1]) == None:
            friends[temp[1]] = "None"
    else:
        friends[temp[0]] = "None"

entered = list(input().split())

def search(key):
    global in_circle
    if friends[key] == entered[1] or friends[key] == "None":
        in_circle = True
        return
    if friends[key] in found:
        return
    else:
        queue.append(friends[key])

while True:    
    found = [entered[0]]
    
    steps = 0
    if friends.get(entered[0]) == None:
        current = "None"
    else:
        current = friends[entered[0]]
    in_circle = False

    queue = [entered[0]]
    while queue: 
        
        key = queue.pop(0)
        search(key)

        found.append(key)
            
        if not in_circle:
            steps += 1
        
    if in_circle:
        print("Yes", steps)
    else:
        print("No")

    entered = list(input().split())
    if entered[0] == '0' and entered[1] == '0':
        break

