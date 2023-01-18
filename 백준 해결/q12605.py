# https://www.acmicpc.net/problem/12605
# 파이썬 다 까먹었다 ㅋㅋㅋ 큰일남
N = int(input())
for i in range(N):
    str = list(input().split())
    print("Case #", end='')
    print((i+1), end='')
    print(":", end=' ')
    for i in range(len(str)):
        print(str.pop(), end=' ')