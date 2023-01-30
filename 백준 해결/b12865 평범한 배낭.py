import sys
input = sys.stdin.readline

N, K = map(int, input().split(' '))

items = list()
for n in range(N):
    W, V = map(int, input().split(' '))
    items.append([W, V])

dp = [[0 for i in range(K+1)] for i in range(N+1)]

for i in range(1,N+1):
    for j in range(1,K+1):
        if items[i-1][0]>j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(items[i-1][1] + dp[i-1][j-items[i-1][0]], dp[i-1][j])

print(dp[N][K])