# https://www.acmicpc.net/problem/2164

import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
array = deque([i+1 for i in range(N)])

for i in range(N-1):
    array.popleft()
    array.append(array.popleft())

print(array[0])