import math

t = int(input())
k = []
n = []

for i in range(t):
  k.append(int(input()))
  n.append(int(input()))

result = []
for i in range(t):
  nCr = math.factorial(k[i] + n[i]) // (math.factorial(n[i] - 1) * math.factorial(k[i] + 1))
  result.append(nCr)

for i in range(t):
  print(result[i])