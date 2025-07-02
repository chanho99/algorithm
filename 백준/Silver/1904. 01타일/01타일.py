def dp(a):
    tile = [0] * (a + 2)

    tile[1] = 1
    tile[2] = 2

    if a != 1 and a != 2:
        for i in range(3, a+1):
            tile[i] = (tile[i-1] + tile[i-2]) % 15746

    return tile[a]

n = int(input())
print(dp(n))