import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
picture = list()

for n in range(N):
    picture.append(list(input().rstrip()))

move_x = [1, -1, 0, 0]
move_y = [0, 0, 1, -1]

def dfs(visited, x, y, color):
    if not(0<=x<N and 0<=y<N):
        return
    elif visited[x][y] or picture[x][y]!=color:
        return
    else:
        visited[x][y] = True
        for i in range(4):
            if 0<=move_x[i]+x<N and 0<=move_y[i]+y<N:
                dfs(visited, move_x[i]+x, move_y[i]+y, color)

visited = [[False for n in range(N)] for n in range(N)]
cnt = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt+=1
            dfs(visited, i, j, picture[i][j])

print(cnt, end=' ')

for i in range(N):
    for j in range(N):
        if picture[i][j]=='G':
            picture[i][j]='R'

visited = [[False for n in range(N)] for n in range(N)]
cnt = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt+=1
            dfs(visited, i, j, picture[i][j])

print(cnt, end=' ')