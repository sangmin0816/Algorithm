# https://www.acmicpc.net/problem/1920
# 이분탐색 binary search
import sys
input = sys.stdin.readline

N = int(input())
Narray = list(map(int, input().split(' ')))
M = int(input())
Marray = list(map(int, input().split(' ')))

Narray.sort()

def binarySearch(i, Narray, left, right):
    while(left<=right):
        mid = (left+right)//2
        if i > Narray[mid]:
            left = mid+1
        elif i < Narray[mid]:
            right = mid-1
        elif i == Narray[mid]:
            return True
    return False

for i in Marray:
    left = 0
    right = len(Narray)-1
    if binarySearch(i, Narray, left, right):
        print(1)
    else:
        print(0)