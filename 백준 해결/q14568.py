# https://www.acmicpc.net/problem/14568

import sys
input = sys.stdin.readline

N = int(input())
ans = 0

for B in range(1, N-4):
    for C in range(B+2, N-B):
        A = N-B-C
        if(A%2==0):
            if(A+B+C==N):
                ans+=1

print(ans)