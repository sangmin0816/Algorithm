# 오래 전에 재귀로 풀려다가 고전한 문제
# 문제만 잘 읽어도 답을 맞출 수 있다. 문제가 곧 힌트였다.
# acmicpc.net/problem/14606

import sys
input = sys.stdin.readline

N = int(input())

pizza = [0 for i in range(N+3)]
pizza[2]=1

for i in range(2, N+1):
    if(i%2==0):
        pizza[i] = pizza[i//2]*2 + (i//2)**2
    else:
        pizza[i] = pizza[i//2]+pizza[i//2+1] + (i//2) * (i//2+1)

print(pizza[N])