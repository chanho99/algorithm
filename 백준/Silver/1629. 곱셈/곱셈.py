a, b, c = map(int, input().split())
d = 1

while b > 0:
    if b % 2 == 1:
        d = (d * a) % c
    a = (a * a) % c
    b //= 2

print(d)