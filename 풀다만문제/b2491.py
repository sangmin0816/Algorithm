import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split(' ')))

dp_up = [1]*(N+1)
dp_down = [1]*(N+1)

for i in range(1, N):
    if arr[i]>=arr[i-1]:
        dp_up[i] = dp_up[i-1]+1 # 연속 상승인 경우
    if arr[i]<=arr[i-1]:
        dp_down[i] = dp_down[i-1]+1 # 연속 하강인 경우
    
    # 연속이 깨지면 dp[i-1]이 1이 되면서 초기화 됨.
        
print(max(max(dp_up), max(dp_down)))