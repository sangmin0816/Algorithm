# ★ 시간 초과가 자꾸 났다.
# 9번을 풀었다... 

import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

arrA = [int(input()) for i in range(N)]
arrA.sort()

def binarySearch(arr, key): # 시간 초과가 참으로 많이 났다
    left = 0
    right = len(arr)-1
    
    while right >= left:
        mid = (left+right)//2
        if arr[mid] == key: 
            # 동일한 값들에 대해 최소 인덱스 찾는 것도 이진탐색으로 해야 시간 초과가 안 남
            if mid==0 or arr[mid-1]!=key:
                return mid
            right = mid-1
        elif arr[mid] > key:
            right = mid - 1
        elif arr[mid] < key:
            left = mid + 1
    
    return -1

for i in range(M):
    q = int(input())
    a = binarySearch(arrA, q)
    print(a)