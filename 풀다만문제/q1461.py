import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

arr = list(map(int, input().split(' ')))
ans = 0

arr.sort()

while(len(arr)):
    ans+=arr.pop()*2


arr.sort(reverse=True)