# https://www.acmicpc.net/problem/3986
import sys
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for i in range(N)]

ans = N


for i in words:
    temp = []
    for j in i:
        if not len(temp):
            temp.append(j)
        else:
            popped = temp.pop()
            if j != popped:
                temp.append(popped)
                temp.append(j)
    if len(temp):
        ans-=1

print(ans)