import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

A.sort()
B.sort(reverse=True)

ans = 0
for n in range(N):
    ans += A[n]*B[n]

print(ans)