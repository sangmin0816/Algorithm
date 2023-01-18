from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
illust = [list(map(int, input().split(' '))) for i in range(n)]

def bfs(i, j):
    visited = [[0]*m]*n
    visited[i][j] = 0
    q = deque()
    q.append([i, j])