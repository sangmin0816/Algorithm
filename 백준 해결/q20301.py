from collections import deque
import sys
input = sys.stdin.readline # 이거 하나만으로도 시간 초과가 날 수 있다

N, K, M = map(int, input().split(' '))

arr = deque([i+1 for i in range(N)])

flag = True
while(len(arr)):
    if flag :
        for i in range(K-1):
            arr.append(arr.popleft())
        print(arr.popleft())
    if not flag:
        for i in range(K-1):
            arr.appendleft(arr.pop())
        print(arr.pop())
    if len(arr)%M == N%M:
        flag = not flag
    