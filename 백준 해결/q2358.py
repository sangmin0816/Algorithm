# 이 질문을 읽어서 정말 다행이었다 https://www.acmicpc.net/board/view/83686
# (1, 0), (2, 0), (3, 0)과 같이 직선이 겹치게 되면 하나로 판단하는 거였다. 하지만 같은 두 점이면 직선이 2개다
# 너저분한 문제이다

import sys
input = sys.stdin.readline

n = int(input())

ans = 0

parallelx = dict()
parallely = dict()

for i in range(n):
    x, y = map(int, input().split(' '))
    if x in parallelx:
        parallelx[x] += 1
    else:
        parallelx[x] = 1
    if y in parallely:
        parallely[y] += 1
    else:
        parallely[y] = 1

for i in parallelx.values():
    if i>1:
        ans+=1

for i in parallely.values():
    if i>1:
        ans+=1

print(ans)