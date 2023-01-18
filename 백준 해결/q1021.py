# 어느쪽이 더 가까운 방향일지 정하는게 어려웠다. 그래서 일단 돌리면서 카운트한 후 비교 후처리했다.
# https://www.acmicpc.net/problem/1021

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

que = deque(i+1 for i in range(N))

removal = list(map(int, input().split(' ')))

ans = 0
for i in removal:
    if que[0] == i:
        que.popleft()
    else:
        temp = que.pop()
        cnt = 1
        while(temp!=i):
            que.appendleft(temp)
            temp = que.pop()
            cnt+=1
        if(cnt>(len(que)+1)/2):
            ans+=(len(que)+1-cnt)
        else:
            ans+=cnt

print(ans)