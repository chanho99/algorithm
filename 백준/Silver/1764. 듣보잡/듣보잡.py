n, m = map(int, input().split())

hear = set(input() for _ in range(n))
see = set(input() for _ in range(m))

result = sorted(hear & see)

print(len(result))
for name in result:
    print(name)