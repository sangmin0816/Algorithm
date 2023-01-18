import sys
input = sys.stdin.readline

Q = int(input())

ans = 0

employees = dict()
ans = 0

for q in range(Q):
    record = list(input().split(' '))
    name = record[0]
    status = record[1]

    if name not in employees:
        employees[name] = []
    
    if len(status):
        employees[name].append(status)
    elif status == '-' and status.pop() == '+':
        continue
    else:
        employees.append('-')