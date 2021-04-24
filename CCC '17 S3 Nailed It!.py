import sys
input = sys.stdin.readline
N = int(input())

counter = [0 for i in range(2000)]
sums = [0 for i in range(4000)]

planks = list(map(int, input().split()))

for i in range(N):
    counter[planks[i] - 1] += 1

for i in range(2000):
    for j in range(i, 2000):
        if counter[i] != 0 and counter[j] != 0:
            if i == j:
                sums[i + j + 1] += counter[i] // 2
            else:
                sums[i+ j + 1] += min(counter[i], counter[j])


sums.sort()
count = 0
length = sums[-1]
for i in range(len(sums)-1, -1, -1):
    if sums[i] == length:
        count += 1
print(length, count)