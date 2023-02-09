# 정말 간단한 문제였는데, 이상한 문제에서 헤매서 시간을 엄청엄청 잡먹었다 서러워
import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
r, c, d = map(int, input().split(' '))

room = list()
for n in range(N):
    room.append(list(map(int, input().split(' '))))

move_x = [-1, 0, 1, 0]
move_y = [0, 1, 0, -1]

def dfs(x, y, d, room):
    visited = [[False for m in range(M)]for n in range(N)]
    stack = [[x, y]]
    cnt = 0

    while stack:
        nx, ny = map(int, stack.pop())
        flag = True
        if not visited[nx][ny]:
            visited[nx][ny] = True
            cnt+=1

        for i in range(4):
            d = (d-1)%4
            if not visited[nx+move_x[d]][ny+move_y[d]] and room[nx+move_x[d]][ny+move_y[d]]==0:
                stack.append([nx+move_x[d], ny+move_y[d]])
                flag = False
                break
        
        if flag:
            temp = (d-2)%4
            if room[nx+move_x[temp]][ny+move_y[temp]]==1:
                return cnt
            else:
                stack.append([nx+move_x[temp], ny+move_y[temp]])

print(dfs(r, c, d, room))