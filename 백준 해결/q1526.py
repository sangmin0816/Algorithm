#의외로 시간 초과가 안 났다

import sys
input = sys.stdin.readline

N = int(input())

for i in range(N, 3, -1):
    temp = set(list(map(int, str(i))))
    if not len(temp - set([4, 7])):
        print(i)
        break