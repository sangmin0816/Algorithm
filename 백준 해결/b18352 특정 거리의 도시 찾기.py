#BFS로 전환하니깐 시간초과 해결 진짜 쫄렸다

from collections import deque
import sys
input = sys.stdin.readline
INF = 300000

N, M, K, X = map(int, input().split(' '))

cities_edge = [[] for n in range(N+1)]
distance = [INF for n in range(N+1)]
visited = [False for n in range(N+1)]

for m in range(M):
    A, B = map(int, input().split(' '))
    cities_edge[A].append(B)

def get_smallest_node():
    min_val = INF
    index = 1
    for i in range(1, N+1):
        if (not visited[i]) and distance[i] < min_val:
            min_val = distance[i]
            index = i
    
    return index

def dijkstra(start):
    distance[start] = 0
    que = deque([start])

    while que:
        now = que.popleft()
        if not visited[now]:
            visited[now] = True
            for i in cities_edge[now]:
                if distance[now]+1 < distance[i]:
                    distance[i] = distance[now]+1
            
            que.extend(cities_edge[now])

dijkstra(X)


flag = True
for n in range(1, N+1):
    if distance[n]==K:
        print(n)
        flag = False

if flag:
    print(-1)