#https://www.acmicpc.net/problem/6131

import sys
input = sys.stdin.readline

N = int(input())

ans = 0

for A in range(int((N+1)**(1/2)), 500):
    for B in range(1, A):
        if((A**2)-(B**2)==N):
            ans+=1

print(ans)