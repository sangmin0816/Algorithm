import sys
input = sys.stdin.readline

N, K = map(int, input().split(' '))

coins = list()
for n in range(N):
    coins.append(int(input()))

dp = [0 for i in range(K+1)]

for i in range(N):
    for j in range(1, K+1):
        if j==coins[i]:
            dp[j] = dp[j]+1
        elif j>coins[i]:
            dp[j] = dp[j]+dp[j-coins[i]]

print(dp[K])