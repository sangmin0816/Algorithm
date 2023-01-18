# 망할 놈의 피보나치 수열
import sys
input = sys.stdin.readline

N = int(input())

dp = [0, 1, 1, 2, 3, 5, 8]

for i in range(6, N):
    dp.append(dp[-1]+dp[-2])

print(dp[N])