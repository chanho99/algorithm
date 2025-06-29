a, b = map(int, input().split())
board = []

for i in range(a):
  board.append(input())

black = ['BWBWBWBW', 'WBWBWBWB'] * 4
white = ['WBWBWBWB', 'BWBWBWBW'] * 4

result = float('inf')

for i in range(a - 7):
  for j in range(b - 7):
    changeB = 0
    changeW = 0
    for k in range(8):
      for l in range(8):
        if board[i+k][j+l] != black[k][l]:
          changeB += 1
        if board[i+k][j+l] != white[k][l]:
          changeW += 1
    result = min(result, changeB, changeW)

print(result)