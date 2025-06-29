n = int(input())
a = list(map(int, input().split()))
b = []

m = 0
for i in range(n):
  if a[i] > m:
    m = a[i]

for i in range(n):
  b.append(a[i] / m)

total = 0
for i in range(n):
  total += b[i]

result = total / n * 100
print(result)