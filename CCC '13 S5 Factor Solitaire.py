N, p, input = int(input()), 0, __import__('sys').stdin.readline
while N!= 1:
    for i in range(2, N+1):
        if N % i == 0: p +=  (N - N//i) // (N//i); N = N - N//i; break
print(p)