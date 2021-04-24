N = int(input())
for _ in range(N):
    s = input()
    sub = (len(s) * (len(s) + 1)) //2
    arr = sorted(s[i:] for i in range(len(s)))
    repeats = [0] * len(arr)
    for i in range(1, len(arr)):
        count = 0
        for j in range(min(len(arr[i]), len(arr[i-1]))):
            if arr[i][j] == arr[i-1][j]:
                count += 1
            else:
                break
        repeats[i] = count
    print(sub - sum(repeats)+1)