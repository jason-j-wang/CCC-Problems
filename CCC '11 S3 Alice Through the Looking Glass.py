import sys
input = sys.stdin.readline

grid = [[0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]

def crystal(mag, index):
    row, col = index
    r = int(row / 5**mag)
    c = int(col / 5**mag)
    if (c, r) == (1, 1) or (c, r) == (2, 2) or (c, r) == (1, 3):
      return crystal(mag -1, [row % (5**mag), col % (5 ** mag)])

    else:
      return grid[c][r] == 1
  
for i in range(int(input())):
  mag, row, col = list(map(int, input().split()))
  print("crystal") if crystal(mag-1, [row, col]) else print("empty")