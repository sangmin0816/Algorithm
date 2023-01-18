# 시간초과 해결하기

import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

heaps = []

for i in range(M):
    n = int(input())
    m = list(map(int, input().split(' ')))
    heaps.append(m)

num = 0
for i in range(1, N+1):
    for j in heaps:
        if len(j) and j[len(j)-1]==i:
            j.pop()
            num+=1
    if(i!=num):
        print("No")
        sys.exit(0)

print("Yes")        