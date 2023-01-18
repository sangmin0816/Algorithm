#https://www.acmicpc.net/problem/1977

import math
import sys
input = sys.stdin.readline

M = int(input())
N = int(input())
ans = []

for i in range(math.ceil(math.sqrt(M)), math.floor(math.sqrt(N))+1):
    ans.append(i**2)

if not len(ans):
    print(-1)
else:
    print(sum(ans))
    print(ans[0])