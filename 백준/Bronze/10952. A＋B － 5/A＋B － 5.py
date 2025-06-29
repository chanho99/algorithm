a, b = [], []

while True:
  c, d = map(int, input().split())
  if c == 0 and d == 0:
    break
  a.append(c)
  b.append(d)

for i in range(len(a)):
  print(a[i] + b[i])