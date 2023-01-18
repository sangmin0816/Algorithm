import sys
input = sys.stdin.readline

n=int(input())

answer = 0
length = len(str(n))

if(n!=1):
    for i in range(9*length, 0, -1):
        temp = n-i
        cnt = 0
        while(temp>0):
            cnt = cnt+temp%10
            temp = temp//10
        if(cnt == i):
            answer = n-i
            break

print(answer)