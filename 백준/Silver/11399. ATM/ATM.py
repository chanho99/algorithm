n = int(input())
p = list(map(int, input().split()))

p.sort()
plus = 0
result = 0

for i in range(n):
    plus += p[i]
    result += plus

print(result)