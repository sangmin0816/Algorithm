import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

maze = [input() for i in range(N)]
print(maze)
