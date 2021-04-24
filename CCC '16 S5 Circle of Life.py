N, T = map(int, input().split())
cells = [int(c) for c in input()]
new_cells = [0] * N

for i in reversed(range(50)):
    if (T >> i) & 1:
      num = 2 ** i
      for cell in range(N):
            new_cells[cell] = (cells[(cell + num) % N] ^ cells[(cell - num) % N])
      cells = new_cells.copy()
print("".join(str(cell) for cell in new_cells))