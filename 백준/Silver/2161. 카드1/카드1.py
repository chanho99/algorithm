n = int(input())
a = list(range(1, n+1))
b = []

while len(a) > 0:
  b.append(a.pop(0))
  if len(a) > 0:
    a.append(a.pop(0))

print(*b)