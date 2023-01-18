import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    a, b = map(int, input().split(' '))

    # 최대공약수
    bmin = b
    amin = a
    while(bmin%amin != 0):
        nmin = bmin%amin
        bmin = amin
        amin = nmin
    
    print(a*b//amin, amin)
    #최대공배수: a*b//최대공약수