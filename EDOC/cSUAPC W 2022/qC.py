# C번 89

import sys
input = sys.stdin.readline

N = int(input())

interest = list(map(int, input().split(' ')))
register = list(map(int, input().split(' ')))

print(sum(interest))

ans = 0
for i in range(len(interest)):
    if(not register[i]):
        ans += interest[i]

print(ans)