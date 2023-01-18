import sys
input = sys.stdin.readline

N = int(input())

fib = [0, 1, 1]

fib_recur = ((((1+5**(1/2))/2)**N - ((1-5**(1/2))/2)**N)/(5**(1/2)))%1000000007
fib_dp = (N-2)%1000000007

print(round(fib_recur), fib_dp)

# 오버 플로우 해결 못함