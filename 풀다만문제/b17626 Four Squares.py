import sys
input = sys.stdin.readline

n = int(input())

divisor = n**(1/2)
if divisor.is_integer():
    print(1)
    sys.exit(0)

for i in range(1, int(divisor)):
    for j in range(1, int(divisor)):
        if i**2+j**2 == n:
            print(2)
            sys.exit(0)

for i in range(1, int(divisor)):
    for j in range(1, int(divisor)):
        for k in range(1, int(divisor)):
            if i**2+j**2+k**2 == n:
                print(3)
                sys.exit(0)

print(4)