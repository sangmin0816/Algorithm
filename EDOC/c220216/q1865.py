# 최상민 1865 웜홀
# https://letalearns.tistory.com/78

import sys
input = sys.stdin.readline

def bf(start): # 벨만 포드
    dist[start] = 0
    for i in range(1, n+1): # 경로의 길이
        for s in range(1, n+1): # 노드 s에 대하여
            for next, time in graph[s]: 
                if dist[next] > dist[s] + time: # s를 거쳐가는 게 더 빠르면
                    dist[next] = dist[s] + time # 값을 갱신
                    if i == n: #경로의 최대 길이, n-1번 지나면 음수 사이클 존재.
                        return True # 음수 사이클 존재
    return False # 음수 사이클 없음

TC = int(input())
for i in range(TC):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n+1)] # 간선 집합
    dist = [10001 for _ in range(n+1)] # 노드까지 거리의 최소값. 최대값인 10001로 초기화
    for j in range(m):
        s, e, t = map(int, input().split())
        graph[s].append([e, t])
        graph[e].append([s, t])
    for k in range(w):
        s, e, t = map(int, input().split())
        graph[s].append([e, -t])

    negative_cycle = bf(1)
    if not negative_cycle: # 음수 사이클이 안 생기면
        print("NO")
    else: # 음수 사이클이 생기면
        print("YES")