#https://www.acmicpc.net/problem/2606 바이러스

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
pair = int(input())

edge = [[] for i in range(n+1)]

for i in range(pair):
    v, w = map(int, input().split(' '))
    edge[v].append(w)
    edge[w].append(v)

visited = [0 for i in range(n+1)]

def bfs(node):
    temp = deque()
    temp.append(node)
    visited[node] = 1
    while(temp):
        node = temp.popleft()
        for i in edge[node]:
            if(visited[i]==0):
                visited[i]=1
                temp.append(i)

bfs(1)
print(visited.count(1)-1) # 1 자기 자신을 빼줘야 함