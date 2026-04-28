stairs = [0]

def stair(n):
    global dp
    if dp[n] != None:
        return dp[n]
    if n == 1:
        dp[n] =  stairs[1]
    elif n == 2:    
        dp[n] = stairs[1] + stairs[2]
    elif n == 3:
        dp[n] = max(stairs[1], stairs[2]) + stairs[3]
    else:
        dp[n] = max(stair(n - 2), stair(n - 3) + stairs[n - 1]) + stairs[n]
    return dp[n]

n= int(input())
dp = [None] * (n + 1)
for i in range(n):
    stairs.append(int(input()))

print(stair(n))
