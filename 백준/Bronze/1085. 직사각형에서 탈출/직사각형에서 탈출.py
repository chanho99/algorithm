x, y, w, h = map(int, input().split())

tmp = [x, y, w-x, h-y]
result = min(tmp)

print(result)