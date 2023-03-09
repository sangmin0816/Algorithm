import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    K = int(input())
    N = int(input())

    apartment = [[0 for n in range(N+1)] for k in range(K+1)]
    
    for n in range(N+1):
        apartment[0][n] = n

    for k in range(1, K+1):
        for n in range(1, N+1):
            apartment[k][n] = apartment[k-1][n] + apartment[k][n-1]
    
    print(apartment[-1][-1])