n = int(input())
coordinate = []

for i in range(n):
  a, b = map(int, input().split())
  coordinate.append((a, b))

coordinate.sort()
for i in range(n):
  for j in range(2):
    print(coordinate[i][j], end=' ')
  print()