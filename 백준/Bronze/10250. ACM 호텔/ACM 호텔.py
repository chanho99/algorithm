t = int(input())

h = []
w = []
n = []

for _ in range(t):
    a, b, c = map(int, input().split())
    h.append(a)
    w.append(b)
    n.append(c)

result = []

for i in range(t):
    if n[i] % h[i] == 0:
        num = n[i] // h[i] + h[i] * 100
    else:
        num = (n[i] // h[i] + 1) + (n[i] % h[i] * 100)
    result.append(num)

for i in range(t):
    print(result[i])