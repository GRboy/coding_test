testcase = int(input())

while testcase > 0:
    testcase -=1

    n,m = map(int,input().split())
    array = list(map(int,input().split()))
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m

    for y in range(1,m):
        for x in range(n):
            maximum = 0
            if x == 0:
                maximum=max(dp[0][y-1],dp[1][y-1])
            elif x == n-1:
                maximum=max(dp[n-2][y-1],dp[n-1][y-1])
            else:
                maximum=max(dp[x-1][y-1],dp[x][y-1],dp[x+1][y-1])
            dp[x][y] += maximum

    maximum = 0
    for i in range(n):
        if maximum < dp[i][m-1]:
            maximum = dp[i][m-1]
    print(maximum)
