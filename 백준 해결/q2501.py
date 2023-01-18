# 왜 98%에서 자꾸 인덱스 에러가 발생할까..
# 제발 좀 맞알 벌써 한 시간째 푼다... 제곱근 쓰지 말고 반복문 겁내 돌릴 걸
# https://www.acmicpc.net/problem/2501

import sys
input = sys.stdin.readline

N, K = map(int, input().split(' '))

divisor = []

for i in range(1, int(N**(1/2)+1)):
    if(N%i==0):
        divisor.append(int(i))
        divisor.append(int(N/i))

length = len(divisor)
divisor.sort()
if(length>1):
    if(int(N**(1/2))==N**(1/2)):
        divisor.pop(length//2)
        length-=1

if(length<K):
    print(0)
else:
    divisor.sort()
    print(divisor[K-1])