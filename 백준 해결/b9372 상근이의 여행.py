# 비행기 타는 횟수가 아니라 비행기의 종류!!!!! 이므로 그냥 간선의 갯수만 세주면 된다.
# 비행기 타는 횟수 알고리즘 생각한다고 2시간 썼는데 허망하다.

import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N, M = map(int, input().split(' '))

    for m in range(M):
        a, b = map(int, input().split(' '))
    
    print(N-1)