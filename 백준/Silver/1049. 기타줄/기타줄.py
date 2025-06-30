n, m = map(int, input().split())
a = []
b = []

for i in range(m):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

if min(a) >= 6 * min(b):
    result = n * min(b)

elif min(a) < 6 * min(b):
    result = n // 6 * min(a) + min(n % 6 * min(b), min(a))

print(result)