import sys
input = sys.stdin.readline

def bf(start):
    distance[start]=0
    for i in range(1, n+1):
        for sp in range(1, n+1):
            for ep, time in graph[sp]:
                if(distance[ep] > distance[sp]+time):
                    distance[ep] = distance[sp]+time
                    if(i==n):
                        return True
    return False

N, M = map(int, input().split(' '))

distance = [100001]*(N+1)
graph = [[] for i in range(N+1)]

for i in range(M):
    n, m, t = map(int, input().split(' '))
    graph[n].append([m, t])
    graph[m].append([n, t])

if(bf(1)):
    print(-1)
else:
    for i in range(2, N+1):
        print(distance[i])