# https://www.acmicpc.net/problem/10845

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
nqueue = deque()

def queue_udf(n):
    if len(n)>1: # append인 경우
        nqueue.append(int(n[1]))
    elif n[0] == 'size':
        print(len(nqueue))
    else:
        n = n[0]
        length = len(nqueue)
        if length:
            if n == 'front':
                print(nqueue[0])
            elif n == 'back':
                print(nqueue[-1])
            elif n == 'pop':
                print(nqueue.popleft())
            elif n == 'empty':
                print(0)
        else:
            if n == 'empty':
                print(1)
            else:
                print(-1)

for i in range(N):
    n = list(input().strip().split(' '))
    queue_udf(n)