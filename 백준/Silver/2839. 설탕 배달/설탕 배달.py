n = int(input())
count = 0

if n == 4 or n == 7:
    print(-1)
    exit()

while n >= 0:
    if n < 15 and n % 3 == 0:
        count += n // 3
        break
    n -= 5
    count += 1

print(count)