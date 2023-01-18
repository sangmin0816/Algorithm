#https://www.acmicpc.net/problem/9575
#set()가 최고야

import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    A = list(map(int, input().split(' ')))
    
    M = int(input())
    B = list(map(int, input().split(' ')))

    K = int(input())
    C = list(map(int, input().split(' ')))

    total = set()
    for a in A:
        for b in B:
            for c in C:
                total.add(a+b+c)

    ans = list()
    for i in total:
        temp = set(list(str(i)))
        num = ['0', '1', '2', '3', '4', '6', '7', '9']
        flag = True
        for j in temp:
            if j in num:
                flag = False
                break
        if flag:
            ans.append(i)

    print(len(ans))