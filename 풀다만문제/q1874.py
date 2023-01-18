import sys
input = sys.stdin.readline

n = int(input())
stack = [i for i in range(n, -1, -1)]
ans = []

for i in range(n):
    stack_in = int(input())
    temp = stack.pop()
    while(temp<stack_in):
        ans.append('+')
    