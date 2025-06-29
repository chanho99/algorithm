s = input()
result = []
for ch in range(ord('a'), ord('z') + 1):
  search = chr(ch)
  index = s.find(search)
  result.append(index)
print(*result)