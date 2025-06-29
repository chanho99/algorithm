import math

def com(n, r):
  return math.factorial(int(n)) // (math.factorial(int(r)) * math.factorial(int(n-r)))

t = input()
t = int(t)

n, m = [], []

for i in range(t):
  n_val, m_val = input().split()
  n.append(int(n_val))
  m.append(int(m_val))

result = []
for i in range(t):
  result.append(com(m[i], n[i]))
  print(result[i])