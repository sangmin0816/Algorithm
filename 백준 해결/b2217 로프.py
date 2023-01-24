import sys
input = sys.stdin.readline

N = int(input())
ropes = list()

for n in range(N):
    ropes.append(int(input()))

ropes.sort()

ans = list()

for n in range(N):
    ans.append((N-n)*ropes[n])

print(max(ans))