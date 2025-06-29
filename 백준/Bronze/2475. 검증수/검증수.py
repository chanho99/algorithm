a = list(map(int, input().split()))
total = a[0] ** 2 + a[1] ** 2 + a[2] ** 2 + a[3] ** 2 + a[4] ** 2
result = total % 10
print(result)