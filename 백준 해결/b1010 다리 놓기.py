import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    M, N = map(int, input().split(' '))

    den = 1
    num = 1

    for i in range(N, N-M, -1):
        num=num*i//den
        den += 1
    
    print(num)