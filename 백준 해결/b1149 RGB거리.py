import sys
input = sys.stdin.readline

N = int(input())
costs = list()
for n in range(N):
    R, G, B = map(int, input().split(' '))
    costs.append([R, G, B])

dp = [[0, 0, 0] for n in range(N)]
dp[0] = costs[0]

for n in range(1, N):
    dp[n][0] = costs[n][0]+min([dp[n-1][1], dp[n-1][2]])
    dp[n][1] = costs[n][1]+min([dp[n-1][0], dp[n-1][2]])
    dp[n][2] = costs[n][2]+min([dp[n-1][0], dp[n-1][1]])

print(min(dp[N-1]))