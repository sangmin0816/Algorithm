#최상민 Python https://www.acmicpc.net/problem/2841 외계인의 기타 연주
#문제가 무슨 소리인지 이해하기 어려웠다.

import sys
input = sys.stdin.readline # 이거 안했다고 시간 초과라니 너무하다 진짜

N, P = map(int, input().split(' '))

lines = [[0] for i in range(7)] # 줄은 6개지만 편의상 7개씩 빈 이중배열 생성
ans = 0

for i in range(N):
    n, p = map(int, input().split(' ')) # 줄과 프랫    
    if(len(lines[n])==1): #편의상 0 넣은 채로 시작. 줄의 첫 프랫
        lines[n].append(p)
        ans+=1
    else:
        if(lines[n][-1]>p): # 만약 더 작은 프랫 입력 시
            while(lines[n][-1]>p): # 스택이 작거나 같아질 때까지 뺌
                lines[n].pop(-1)
                ans+=1
        if(lines[n][-1]==p): # 만약 프랫이 같다면
            continue # 손가락 안 움직이므로 스킵
        lines[n].append(p)
        ans+=1

print(ans)