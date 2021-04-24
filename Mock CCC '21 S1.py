vowels = ['a', 'e', 'i', 'o', 'u', 'y']
length, max_c, max_v = list(map(int, input().split()))
s = input()

valid = True
i = 0
c, v = 0, 0

while valid and i < length:
    if s[i] != 'y':
        if s[i] in vowels:
            v += 1
            c = 0
        else:
            v = 0
            c += 1
    else:
        c += 1
        v += 1

    if c > max_c or v > max_v:
        valid = False

    i += 1

print("YES" if valid else "NO")