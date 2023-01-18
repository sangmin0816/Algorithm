from re import L
import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

moon = [list(map(input().split(' '))) for i in range(N)]

direction = [-1, 0, 1]
dp = [[101]*M]*N
