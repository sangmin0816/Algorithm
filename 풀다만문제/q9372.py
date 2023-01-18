import sys
input = sys.stdin.readline

def dfs(graph, root):
    visited = []
    stack = [root]
    cnt = 0
    
    while len(visited)!=len(graph):
        now = stack.pop()
        if now not in visited:
            visited.append(now)
            stack.extend(graph[now])
        cnt += 1
    
    print(cnt)


T = int(input())
for i in range(T):
    N, M = map(int, input().split(' '))
    airplanes = [[] for n in range(N)]
    
    for m in range(M):
        start, end = map(int, input().split(' '))
        start -= 1
        end -= 1
        airplanes[start].append(end)
        airplanes[end].append(start)
    
    for n in range(N):
        dfs(airplanes, n)
        
    