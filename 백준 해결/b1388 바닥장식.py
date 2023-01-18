# https://www.acmicpc.net/problem/1388

import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

tiles = list()

for i in range(N):
    tiles.append(list(input().rstrip()))

ans = 0

visited = [[False for m in range(M)] for n in range(N)]

def dfs(sx, sy):
    if visited[sx][sy]:
        return 0

    now = tiles[sx][sy]
    
    if now =='-':
        for j in range(sy, M):
            if now == tiles[sx][j]:
                visited[sx][j] = True
            else:
                break
    else:
        for i in range(sx, N):
            if now == tiles[i][sy]:
                visited[i][sy] = True
            else:
                break
    
    return 1
    

for n in range(N):
    for m in range(M):
        ans += dfs(n, m)

print(ans)