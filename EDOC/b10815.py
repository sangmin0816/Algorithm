# 숫자 카드 10815
import sys
input = sys.stdin.readline

N = int(input())
Sang = list(map(int, input().split(' ')))
SangGeun = {i: 0 for i in Sang}

M = int(input())
doesHave = list(map(int, input().split(' ')))

for m in doesHave:
    if m in SangGeun:
        print(1, end=' ')
    else:
        print(0, end=' ')