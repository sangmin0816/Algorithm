#https://www.acmicpc.net/problem/2605
#파이썬이 좋긴 좋다
N = int(input())
num = list(map(int, input().split(' ')))
line = []
for i in range(N):
    line.insert(num[i], i+1)

for i in range(N):
    print(line.pop(), end=' ')