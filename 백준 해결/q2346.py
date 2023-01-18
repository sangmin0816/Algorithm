# https://www.acmicpc.net/problem/2346
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
balloons = list(map(int, input().split(' ')))
b_deq = deque()

for i, b in enumerate(balloons):
    b_deq.append([i+1, b])

ans = [b_deq.popleft()]

index = ans[0][1]

while(len(b_deq)):
    while index > 1:
        b_deq.append(b_deq.popleft())
        index -= 1
    while index < 0:
        b_deq.appendleft(b_deq.pop())
        index += 1
    
    ans.append(b_deq.popleft())
    index = ans[-1][1]

for a in ans:
    print(a[0], end=' ')