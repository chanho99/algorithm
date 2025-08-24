import re

a = input()
a = re.split('([^0-9])', a)

i = 1
result = int(a[0])

while i < len(a) and a[i] != '-':
    result += int(a[i+1])
    i += 2

while i+1 < len(a):
    result -= int(a[i+1])
    i += 2

print(result)