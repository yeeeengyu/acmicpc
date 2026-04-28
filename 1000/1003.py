n = int(input())
dp = [0] * (n + 1)
dp[0] = (1, 0)
dp[1] = (0, 1)
for i in range(n):
    a = int(input())
    dp[a][0] = dp[a-1][0] + dp[a-2][0]
    dp[a][1] = dp[a-1][1] + dp[a-2][1]