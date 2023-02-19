from queue import PriorityQueue
import sys
input = sys.stdin.readline

INF = float("inf")

N = int(input())
M = int(input())

graph = [[] for n in range(N+1)]

for m in range(M):
    start, end, cost = map(int, input().split(' '))
    graph[start].append([cost, end])

start, end = map(int, input().split(' '))

distance = [INF for n in range(N+1)]
    
def dijkstra(start, graph, distance):
    distance[start] = 0

    visited = [False for n in range(N+1)]
    que = PriorityQueue() # 중요
    que.put((0, start))

    while not que.empty():
        dist, now = que.get()
        if not visited[now]:
            visited[now] = True
            for cost, goal in sorted(graph[now]):
                distance[goal] = min(distance[now]+cost, distance[goal])
                que.put((distance[goal], goal))

dijkstra(start, graph, distance)
print(distance[end])