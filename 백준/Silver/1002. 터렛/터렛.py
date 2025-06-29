import math

t = int(input())
result = []

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = math.sqrt((abs(x1 - x2) ** 2) + (abs(y1 - y2) ** 2))

    if x1 == x2 and y1 == y2 and r1 == r2:
        result.append(-1)
    elif abs(r1 - r2) < d < r1 + r2:
        result.append(2)
    elif d == abs(r1 - r2) or d == r1 + r2:
        result.append(1)
    else:
        result.append(0)

for i in range(t):
    print(result[i])