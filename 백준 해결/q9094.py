#pypy로 하니깐 통과됨 휴
#https://www.acmicpc.net/problem/9094
import sys
input = sys.stdin.readline

for i in range(int(input())):
    n, m = map(int, input().split(' '))
    ans = 0
    for b in range(1,n):
        for a in range(1, b):
            if((a**2+b**2+m)%(a*b)==0):
                ans+=1
    print(ans)