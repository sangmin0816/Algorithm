# 1449 수리공 항승

import sys
input = sys.stdin.readline

N, L = map(int, input().split(' '))

holes = list(map(int, input().split(' ')))

holes.sort() # 정렬

answer = [] # 테이프의 시작점들

for h in holes:
    if len(answer) == 0: # 아무것도 없으면 일단 테이프 추가
        answer.append(h)
    # 만약 answer의 구멍으로부터 L-1 범위 내의 새로운 구멍이면 pass
    elif h-answer[-1] > L-1: # 아니라면 새로 테이프 추가
        answer.append(h)
        
print(len(answer))