# https://www.acmicpc.net/problem/2910

import operator
import sys
input = sys.stdin.readline

N, C = map(int, input().split(' '))

arr = list(map(int, input().split(' ')))
dict_a = dict()

for a in arr:
    if a not in dict_a:
        dict_a[a] = 1
    else:
        dict_a[a] += 1

arr_dict = sorted(dict_a.items(), key=operator.itemgetter(1), reverse=True)

for i, n in arr_dict:
    for x in range(n):
        print(i, end=' ')