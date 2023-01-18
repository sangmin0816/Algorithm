# 역시 파이썬은 개 사기 언어
import sys
input = sys.stdin.readline

A, B = map(int, input().split(' '))

A = set(list(map(int, input().split(' '))))
B = set(list(map(int, input().split(' '))))

print(len(A-B)+len(B-A))