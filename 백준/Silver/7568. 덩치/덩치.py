n = int(input())
frame = []

for i in range(n):
  a, b = map(int, input().split())
  frame.append((a, b))

rank = [1] * n

for i in range(n):
  for j in range(n):
    if i != j:
      if frame[i][0] < frame[j][0] and frame[i][1] < frame[j][1]:
        rank[i] += 1

print(*rank)