k, n = map(int, input().split())
length = []

for i in range(k):
  input_data = int(input())
  length.append(input_data)

start = 1
last = max(length)

while start <= last:
  mid = (start + last) // 2
  count = 0

  for l in length:
    count += l // mid

  if count >= n:
    start = mid + 1
  
  else:
    last = mid - 1

print(last)