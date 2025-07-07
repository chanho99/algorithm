n, k = map(int, input().split())

coin = [int(input()) for _ in range(n)]

def min_coin(n, k):
    count = 0

    for i in range(n-1, -1, -1):
        if k >= coin[i]:
            count += k // coin[i]
            k = k % coin[i]

    return count

print(min_coin(n, k))