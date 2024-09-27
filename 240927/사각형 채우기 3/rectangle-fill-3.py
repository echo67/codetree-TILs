n= int(input())

dp = [0 for _ in range(n+2)]
dp[0] = 1
dp[1] = 2
dp[2] = 7

for i in range(3, n+1):
    dp[i] = 2 * dp[i-1] + 3 * dp[i-2] 
    for j in range(i-3, -1, -1):
        dp[i] += 2*dp[j]

print(dp[n]%1000000007)