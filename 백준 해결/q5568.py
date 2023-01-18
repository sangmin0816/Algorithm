# 순열로 푸는 것이라고 한다. 한참 딕셔너리로 어떻게 해보려다 안 됐다
# https://www.acmicpc.net/problem/5568

from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
cards = [input().rstrip() for i in range(n)]

cardset = set()
for i in permutations(cards, k):
    cardset.add(''.join(i))

print(len(cardset))