import sys
input = sys.stdin.readline

n = int(input())
stairs = [int(input()) for i in range(n)]

dp = [stairs]*n

flag1 = False
for i in range(2,n):
    for j in range(i, 1, -1):
        if(not flag1 and dp[i][j-1]>dp[i][j-2]):
            dp[i][j]+=dp[i][j-1]
            flag = True
        else:
            dp[i][j]+=dp[i][j-2]
            flag = False
print(dp)
print(dp[n-1][n-1])