n = int(input())
table = list(map(int,input().split()))
dp = [1]*n
table.reverse()
for i in range(1,n):
    for j in range(0,i):
        if table[i] > table[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(n-max(dp))