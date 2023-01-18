# https://www.acmicpc.net/problem/24416
# 결국 dp로 피보나치 구열하기 였다.
import sys
input = sys.stdin.readline

n = int(input())

countDp = n-2
countRecur = [0, 1, 1, 2, 3, 5]
def fib(n):
    if(n<6):
        return
    else:
        for i in range(6, n+1):
            countRecur.append(countRecur[i-1]+countRecur[i-2])

fib(n)
print(countRecur[n], countDp)