n = int(input())
a = []
for i in range(n):
  a.append(input())

for i in range(n):
  count = int(a[i][0])
  text = a[i][2:]

  result = ""
  for j in range(len(text)):
    result += text[j] * count

  print(result)