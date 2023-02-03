import sys
input = sys.stdin.readline

from collections import deque

N, M, V = map(int, input().split(' '))

graph = [[] for i in range(N+1)]
for m in range(M):
    S, E = map(int, input().split(' '))
    graph[S].append(E)
    graph[E].append(S)

def DFS(V, graph):
    visited = list()
    stack = [V]
    
    while stack:
        now = stack.pop()
        if now not in visited:
            visited.append(now)
            for i in sorted(graph[now], reverse=True):
                if i not in visited:
                    stack.append(i)
            
    return visited

for i in DFS(V, graph):
    print(i, end=' ')
print()

def BFS(V, graph):
    visited = []
    queue = deque([V])
    
    while queue:
        now = queue.popleft()
        if now not in visited:
            visited.append(now)
            for i in sorted(graph[now]):
                if i not in visited:
                    queue.append(i)
    
    return visited
                
for i in BFS(V, graph):
    print(i, end=' ')