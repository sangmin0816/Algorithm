import sys
input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    arr.append(float(input()))

dp = arr.copy()
for i in range(1, N):
    dp[i] = max(dp[i-1]*dp[i], dp[i])
    
print('%.3f'%(max(dp))) # 반올림 하라매!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# round 쓰면 틀린다