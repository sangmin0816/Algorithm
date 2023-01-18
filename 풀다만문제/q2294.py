from re import L
import sys
input = sys.stdin.readline

N, k = map(int, input().split(' '))

coins = [int(input()) for i in range(N)]
coins.sort(reverse=True)

dp = [[k//i, k%i] for i in coins]
ans = -1

for i in range(len(dp)):
    if ((dp[i-1][1]//coins[i])+dp[i-1][0])<dp[i][0]:

    if dp[i][1]==0:
        ans = dp[i][0]
        break

print(ans)