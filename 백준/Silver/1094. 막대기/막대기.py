x = int(input())
count = 0
l = 64

while x > 0:
  if x >= l:
    count += 1
    x -= l
  l //= 2

print(count)