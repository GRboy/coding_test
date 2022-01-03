n, m = map(int,input().split())
coin = list()
for _ in range(n):
    coin.append(int(input()))
dp = [10001] *(10000)

dp[0] = 0
for _ in range(n):
    dp[coin[_]] = 1
for i in range(1,m+1):
    if i-coin[0] >= 0:
        min = dp[i-coin[0]]
        for j in range(1,n):
            if i-coin[j] >= 0:
                if min > dp[i-coin[j]]:
                    min = dp[i-coin[j]]
        dp[i] = min +1
if dp[m] <= 10001:
    print(dp[m])
else:
    print(-1)