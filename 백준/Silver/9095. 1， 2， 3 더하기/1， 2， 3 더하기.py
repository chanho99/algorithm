t = int(input())
n = [int(input()) for _ in range(t)]
max_n = max(n)

dp = [0] * (max_n + 1)
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, max_n + 1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for num in n:
    print(dp[num])