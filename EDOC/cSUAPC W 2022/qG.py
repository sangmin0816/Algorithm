# G번 89

import sys
input = sys.stdin.readline

N = int(input())
road = list(input().strip())
ans = 0

for i in range(N//3):
    for j in range(N-(i+1)*3, -1, -1):
        Tree = road[j:j+(i+1)*3].count('T')%3
        Green = road[j:j+(i+1)*3].count('G')%3
        Fence = road[j:j+(i+1)*3].count('F')%3
        Person = road[j:j+(i+1)*3].count('P')%3
        if(not(Tree or Green or Fence or Person)):
            ans+=1

print(ans)