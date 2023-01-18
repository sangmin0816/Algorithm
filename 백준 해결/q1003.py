# append를 써서 문제였다! 테스트 케이스가 여러개 이다보니, append 쓰려면 fibonacci 배열을 초기화해야함
# https://www.acmicpc.net/problem/1003
import sys

input = sys.stdin.readline

T = int(input())

fibonacci = [0, 1, 1]

def fib(N):
    if(N>2):
        for i in range(3, N+1):
            fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
    
    return fibonacci[N]

for i in range(T):
    N = int(input())
    if(N==0):
        print("1 0")
    else:
        fibonacci = [0, 1, 1]
        one = fib(N)
        print(fibonacci[N-1], one)