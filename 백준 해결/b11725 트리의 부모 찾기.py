import sys
input = sys.stdin.readline

N = int(input())
parent = [i for i in range(N+1)]
edges = [[] for i in range(N+1)]

for n in range(N-1):
    s, e = map(int, input().split(' '))
    edges[s].append(e)
    edges[e].append(s)


visited = [False for n in range(N+1)]
stack = [1]

while stack:
    now = stack.pop()
    if not visited[now]:
        visited[now] = True
        
        for edge in edges[now]:
            if not visited[edge]:
                parent[edge] = now
                stack.append(edge)

for i in range(2, N+1):
    print(parent[i])