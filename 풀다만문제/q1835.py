import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
cards = deque([i+1 for i in range(N)])
ans = deque()

for n in range(N, 0, -1):
    ans.appendleft(cards.pop())
    for i in range(n):
        ans.appendleft(ans.pop())


for i in ans:
    print(i, end=' ')