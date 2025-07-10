def prime_number(n):
    arr = [1] * (n+1)
    end = int(n**(1/2))
    arr[0], arr[1] = 0, 0

    for i in range(2, end + 1):
        if arr[i] == 1:
            for j in range(i*i, n+1, i):
                arr[j] = 0

    return arr

n = int(input())
num = list(map(int, input().split()))

arr = prime_number(max(num))
result = 0
for i in num:
    if arr[i] == 1:
        result += 1

print(result)