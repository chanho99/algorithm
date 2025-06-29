n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b_sorted = sorted(b, reverse=True)

s = sum(a * b for a, b in zip(a, b_sorted))
print(s)