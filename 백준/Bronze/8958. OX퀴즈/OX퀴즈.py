n = int(input())
s = []
for i in range(n):
  s.append(input())

for char in s:
  score = 0
  con = 0
  for ch in char:
    if ch == 'O':
      con += 1
      score += con
    else:
      con = 0
  print(score)