# https://www.acmicpc.net/problem/11652

import sys
input = sys.stdin.readline

N = int(input())
num_dict = dict()

for i in range(N):
    n = int(input())
    if n not in num_dict:
        num_dict[n]=0
    num_dict[n]+=1

maximum = max(num_dict.values())

num_lst = sorted(num_dict.keys())

for i in num_lst:
    if num_dict[i] == maximum:
        print(i)
        sys.exit(0)