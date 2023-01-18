# 최상민 Python https://www.acmicpc.net/problem/1325 효율적인 해킹
#https://jinho-study.tistory.com/928 BFS는 영 어려워서 이걸 참고했다.

from collections import deque
import sys
input = sys.stdin.readline

def bfs(node): # bfs 함수
    q = deque()
    q.append(node)
    check[node] = 1 # 방문 여부 표시
    while q:
        node = q.popleft()
        for n in listM[node]:
            if check[n] == 0: #미방문시 방문
                check[n] = 1
                q.append(n) #큐에 추가

N, M = map(int, input().split(' '))
listM = [[] for i in range(N+1)]

for i in range(M): # B가 간선을 가지는 단방향 노드
    A, B = map(int, input().split(' '))
    listM[B].append(A)

res = []
for i in range(1, N+1): #bfs를 통해 각 노드의 길이를 구한다
    check = [0]*(N+1) # 방명록 리스트 생성
    bfs(i) # bfs 돌리기
    res.append(check.count(1)) # 방문 노드 수 세서 res에 추가

m = max(res) # 가장 긴 길이

for i in range(N):
    if res[i] == m: # max와 일치하면 print
        print(i+1, end=' ')

print()