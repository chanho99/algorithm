tmp = []

n = int(input())
for i in range(n):
  a, b = input().split()
  a = float(a)
  tmp.append((a, b))

for a, b in tmp:
  if b == 'kg':
    result = round(a * 2.2046, 4)
    print(f'{result:.4f} lb')
  elif b == 'lb':
    result = round(a * 0.4536, 4)
    print(f'{result:.4f} kg')
  elif b == 'l':
    result = round(a * 0.2642, 4)
    print(f'{result:.4f} g')
  elif b == 'g':
    result = round(a * 3.7854, 4)
    print(f'{result:.4f} l')