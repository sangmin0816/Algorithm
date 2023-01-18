# https://www.acmicpc.net/problem/9322
import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    n = int(input())
    num1 = list(input().strip().split(' '))
    key = dict()
    for i in range(n):
        key[num1[i]] = 0
    
    num2 = list(input().strip().split(' '))
    for i in range(n):
        key[num2[i]] = i

    pwd = list(input().strip().split(' '))
    
    ans = [None for i in range(n)] # ★ N 개의 빈 배열을 만들 땐 이렇게. []*n은 안 되더라.
    
    for i in range(n):
        ans[i] = pwd[key[num1[i]]]
    
    print(' '.join(ans))