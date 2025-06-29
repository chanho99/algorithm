n = int(input())
a = list(map(int, input().split()))

index_a = list(enumerate(a))

index_a.sort(key=lambda x: x[1])

b = [0] * n

for b_index, (index, value) in enumerate(index_a):
  b[index] = b_index

print(*b)