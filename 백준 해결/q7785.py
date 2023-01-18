# 이름을 해시로 사용하는 문제. 딕셔너리 사용. 리스트는 시간 초과 뜸
# https://www.acmicpc.net/problem/7785

import sys
input = sys.stdin.readline

n = int(input())
workers = dict()

for i in range(n):
    name, status = map(str, input().strip().split(' '))
    if (status == 'enter'):
        workers[name]=status
    else:
        del workers[name]

worker_list = list(workers.keys())
worker_list.sort()
worker_list.reverse()

for i in worker_list:
    print(i)