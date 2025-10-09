t = int(input())
n = [int(input()) for _ in range(t)]
p = [0] * (max(n) + 1)

p[1], p[2], p[3], p[4], p[5] = 1, 1, 1, 2, 2

for i in range(6, max(n) + 1):
    p[i] = p[i-1] + p[i-5]

for x in n:
    print(p[x])