from queue import PriorityQueue
import sys
input = sys.stdin.readline
INF = float("inf")

N, M = map(int, input().split(' '))

graph = [[] for n in range(N+1)]
for m in range(M):
    A, B, C = map(int, input().split(' '))
    graph[A].append([C, B])
    graph[B].append([C, A])

def dijstra(start, graph):
    visited = [False]*(N+1)
    cost = [INF]*(N+1)
    cost[start] = 0
    
    que = PriorityQueue()
    que.put((0, start))

    while not que.empty():
        distance, now = que.get()
        if not visited[now]:
            visited[now]=True
            for c, b in sorted(graph[now]):
                cost[b] = min(distance+c, cost[b])
                que.put((cost[b], b))
    
    print(cost[-1])

dijstra(1, graph)