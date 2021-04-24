adj = {}
paths = []

while True:

    path = str(input())

    if path == "**":
        break

    paths.append(path)

    if adj.get(path[0]) == None:
        adj[path[0]] = [path[1]]
    else:
        adj[path[0]].append(path[1])

    if adj.get(path[1]) == None:
        adj[path[1]] = [path[0]]
    else:
        adj[path[1]].append(path[0])

disc_paths = []

for i in range(len(paths)):
    found = False
    queue = ["A"]
    next_queue = []
    traversed = ["A"]

    adj[paths[i][0]].remove(paths[i][1])
    adj[paths[i][1]].remove(paths[i][0])

    while not found:
 
        if not queue:
            
            disc_paths.append(paths[i])
            break

        else:
            for j in range(len(queue)):
                if "B" in adj[queue[j]]:
                    found = True
                    break
                else:
                    for k in range(len(adj[queue[j]])):
                        if adj[queue[j]][k] not in traversed:
                            traversed.append(adj[queue[j]][k])
                            next_queue.append(adj[queue[j]][k])

            queue = [next_queue[i] for i in range(len(next_queue))]
            next_queue = []

    adj[paths[i][0]].append(paths[i][1])
    adj[paths[i][1]].append(paths[i][0])

for i in range(len(disc_paths)):
    print(disc_paths[i])

print("There are", len(disc_paths), "disconnecting roads.")
