# 간단한 문제같지만 엄청 많이 틀렸다. 자바로도, 파이썬으로도
# https://www.acmicpc.net/problem/2748
import sys
input = sys.stdin.readline

n = int(input())
fibonacci = [0, 1, 1]

if(n<3):
    print(fibonacci[n])
    sys.exit(0)

for i in range(3,n+1):
    fibonacci.append(fibonacci[i-1]+fibonacci[i-2])

print(fibonacci[n])