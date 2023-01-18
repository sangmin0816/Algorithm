# 최상민 14425 문자열 집합
# 아니 이게 시간초과가 안 떠???
# https://www.acmicpc.net/problem/14425
import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
ans = 0

arrayS =[] # 기준 문자열
for i in range(N):
    arrayS.append(input())

arrayT = [] # 검증 문자열
for i in range(M):
    arrayT.append(input())

arrayS.sort() # 각 문자열 정렬
arrayT.sort()

for i in arrayT:
    while(len(arrayS) and i>arrayS[0]): # 검증 문자열이 기준 문자열보다 크고 기준 문자열 범위 벗어나지 않으면
        arrayS.pop(0) # 기준 문자열을 pop하여 앞당긴다
    if(len(arrayS) and i==arrayS[0]): # 검증 문자열과 기준문자열이 같다면
        ans+=1

print(ans)