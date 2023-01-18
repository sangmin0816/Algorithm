# https://www.acmicpc.net/problem/1302
# 딕셔너리를 자동정렬이 아니었다. 그리고 sort()가 아닌 sorted(값)을 써야 한다.

import sys
input = sys.stdin.readline

n = int(input())

bSeller = dict()

for i in range(n):
    temp = input().strip()
    if temp not in bSeller:
        bSeller[temp] = 1
    else:
        bSeller[temp] += 1

sales = max(bSeller.values())

for i in (sorted(bSeller.keys())):
    if(bSeller[i]==sales):
        print(i)
        break
