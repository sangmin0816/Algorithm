from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split(' '))

josephus = deque([i+1 for i in range(N)])

print("<", end='')
for i in range(N-1):
    for j in range(K-1):
        josephus.append(josephus.popleft())
    print(josephus.popleft(), end=', ')

print(josephus.popleft(), end='')
print(">", end='')