import sys
input = sys.stdin.readline

N = int(input())

parent = [i for i in range(N+1)]
for n in range(N-1):
    s, e = map(int, input().split(' '))
    if s==1 or e==1:
        parent[s]=1
        parent[e]=1
    elif parent[s]!=s and parent[e]==e:
        parent[e]=s
    elif parent[s]==s and parent[e]!=e:
        parent[s]=e

for i in range(2, N+1):
    print(parent[i])