# https://www.acmicpc.net/problem/16466
# sort 안 쓰고 풀 수 있는 방법이 있을 것 같은데..
N = int(input())
Ai = list(map(int, input().split(' ')))
Ai.sort()

ticket = 1

for i in range(N):
    if(ticket<Ai[i]): break
    else: ticket+=1

print(ticket)