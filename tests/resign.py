n = int(input())
T = [0]
P = [0]
dp = [0]*(n+1)
max_value = 0
for _ in range(n):
    a,b = map(int,input().split())
    T.append(a)
    P.append(b)
for i in range(n,0,-1):
    if T[i]+i <= n+1:
        dp[i] = max(max_value,dp[T[i]+i]+P[i])
        max_value = dp[i]
    else:
        dp[i] = max_value

print(dp[1])
