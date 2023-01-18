# E번 89

import sys
input = sys.stdin.readline

N, K, H, W, D = map(int, input().split(' '))

rides = []
for i in range(N):
    rides.append(list(map(int, input().split(' '))))

ans = []

for i in range(min(H-D, 1), H+D+1):
    for j in range(min(W-D, 1), W+D+1):
        cnt = 0
        for k in rides:
            if(i>=k[0] and i<=k[1] and j>=k[2] and j<=k[3]):
                cnt+=1
        if(cnt>=K):
            ans.append((i, j))

print(ans)