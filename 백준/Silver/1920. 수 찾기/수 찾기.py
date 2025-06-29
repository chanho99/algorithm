import bisect

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

a.sort()

c = [0] * m

for i in range(m):
  tmp = bisect.bisect_left(a, b[i])
  if tmp < n and a[tmp] == b[i]:
    c[i] = 1
  
for i in range(m):
  print(c[i])