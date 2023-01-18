import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    print('Case #%d: '%(t+1), end=' ')

    N = int(input())
    F = list(map(int, input().split(' ')))
    P = list(map(int, input().split(' ')))