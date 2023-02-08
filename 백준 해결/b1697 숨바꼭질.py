import sys
input = sys.stdin.readline

from collections import deque

def bfs(N, K, time):
    que = deque([N])
    while que:
        now = que.popleft()
        if now==K:
            print(time[now])
            return
        next = [now-1]
        if now<K:
            next+=[now+1, now*2]

        for n in next:
            if 0<=n<=100000 and time[n]==0:
                time[n]=time[now]+1
                que.append(n)

N, K = map(int, input().split(' '))

time = [0]*100001

bfs(N, K, time)
