# https://www.acmicpc.net/problem/15995
# 가끔 머리랑 손이 다로 놀아서 틀릴 때도 있다.

import sys
input = sys.stdin.readline

a, m = map(int, input().split(' '))
x = 1
while(True):
    if((a*x)%m==1):
        print(x)
        break
    x+=1