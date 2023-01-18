import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

friends = [set([i]) for i in range(N+1)]

for i in range(M):
    A, B = map(int, input().split(' '))
    print(len(friends[A]^friends[B])//2)
    
    A = B = friends[A].union(friends[B])