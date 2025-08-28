n, m, b = map(int, input().split())
ground = []
count = [0] * 257

for _ in range(n):
    h = list(map(int, input().split()))
    ground.append(h)

for rows in ground:
    for i in rows:
        count[i] += 1

height = max(i for i, v in enumerate(count) if v > 0)
best_height = height
best_time = float('inf')

while height >= 0:
    add = 0
    remove = 0

    for i in range(257):
        if height > i:
            add += (height - i) * count[i]
        elif height < i:
            remove += (i - height) * count[i]

    if remove + b < add:
        height -= 1
        continue

    current_time = add + remove * 2

    if current_time < best_time:
        best_time = current_time
        best_height = height

    if add * 2 < remove:
        break

    height -= 1

print(best_time, best_height)