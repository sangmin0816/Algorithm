import sys
input = sys.stdin.readline

N = int(input())

province = list(map(int, input().split(' ')))
province.sort()

M = int(input())

if M >= sum(province):
    print(province[-1])
else:
    budget = M//N
    remain = 0
    city = 0
    
    for p in province:
        if p<=budget:
            remain += budget-p
        else:
            city += 1

    print((budget*city+remain)//city)