import sys
input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    inner = input().rstrip()
    total = sum(list(map(inner)))
    arr.append([total, inner])


arr.sort()

for i, j in arr:
    print(j)