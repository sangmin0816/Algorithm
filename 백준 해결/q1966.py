# https://www.acmicpc.net/problem/1966

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N, M = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))

    printer = deque()

    for i, num in enumerate(arr):
        printer.append([num, i])

    arr.sort()

    ans = 1
    while True:
        p = printer.popleft()
        a = arr.pop()
        if p[0] == a:
            if p[1] == M:
                print(ans)
                break
            ans+=1
            continue
        else:
            printer.append(p)
            arr.append(a)