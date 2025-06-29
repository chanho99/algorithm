n = int(input())
s = []

for i in range(n):
  s.append(input())

result = []

for i in range(n):
  count = 0
  forBreak = True
  for j in range(len(s[i])):
    if s[i][j] == '(':
      count += 1
    else:
      count -= 1
    if count < 0:
      result.append('NO')
      forBreak = False
      break
  if forBreak == True:
    if count == 0:
      result.append('YES')
    else:
      result.append('NO')

for i in range(n):
  print(result[i])