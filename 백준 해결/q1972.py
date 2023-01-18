# https://www.acmicpc.net/problem/1972
import sys
input = sys.stdin.readline

while(True):
    T = input().rstrip()
    if T == '*':
        break
    
    flag = True
    for i in range(1, len(T)-1):
        surprise = dict()
        for j in range(len(T)-i):
            pair = T[j]+T[j+i]
            if pair not in surprise:
                surprise[pair] = 0
            else:
                flag = False
                break
    if flag:
        print(T,"is surprising.")
    else:
        print(T,"is NOT surprising.")