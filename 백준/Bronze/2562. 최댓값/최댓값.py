a = []

for i in range(9):
  a.append(int(input()))

m = a[0]
n = 0

for i in range(9):
  if a[i] > m:
    m = a[i]
    n = i

print(m)
print(n+1)