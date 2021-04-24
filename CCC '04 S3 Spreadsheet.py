import sys
input = sys.stdin.readline
sheet = [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
is_int = [[False for i in range(10)]for i in range(11)]
numbers = '0123456789'
d = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10}

for i in range(1, 11):
    row = input().split()
    row.insert(0, 0)
    for j in range(1, len(row)):
        if row[j][0] in numbers:
            #print(i, j)
            is_int[i][j] = True
    if len(row)< 10:
        for k in range(len(row)+1, 10):
            row.append("*")
    sheet.append(row)

        
def find_sum(r, c, traversed):
    if is_int[r][c]:
        return int(sheet[r][c])
    if not sheet[r][c] or sheet[r][c] == "*":
        return "*"

    if sheet[r][c] in traversed:
        return "*"
    sums = []

    split = sheet[r][c].split("+")

    for cell in split:
        row = d[cell[0]]
        col = int(cell[1])
        idk = find_sum(row, col, traversed + [sheet[r][c]])
        if idk == "*":
            sheet[row][col] = "*"
            return "*"
        sums.append(int(idk))
    sheet[r][c] = str(sum(sums))
    is_int[r][c] = True
    return sheet[r][c]

for i in range(1, 11):
    for j in range(1, 10):
        if not is_int[i][j]:
            sheet[i][j] = find_sum(i, j, [])

for i in range(1, 11):
    sheet[i].pop(0)
    print(" ".join(sheet[i]))
