num = int(input())
supply =list(map(int,input().split()))
dp = [0]*num
dp[0] = supply[0]
if supply[0] <supply[1]:
    dp[1] = supply[1]
else:
    dp[1] = supply[0]

for i in range(2,num):
    dp[i] = dp[i-2]+supply[i] if dp[i-2]+supply[i] > dp[i-1] else dp[i-1]
print(dp[num-1])