from collections import deque

n = int(input())
a = deque(range(1, n+1))

while len(a) > 1:
  a.popleft()
  if len(a) > 1:
    a.append(a.popleft())

print(a[0])