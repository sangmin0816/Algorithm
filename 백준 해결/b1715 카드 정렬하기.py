import sys
input = sys.stdin.readline
from queue import PriorityQueue

N = int(input())
cards = PriorityQueue()

for n in range(N):
    cards.put(int(input()))

ans = list()

if cards.qsize()==1:
    ans.append(0)

while cards.qsize()>1:
    card_1 = cards.get()
    card_2 = cards.get()
    cards.put(card_1+card_2)
    ans.append(card_1+card_2)

print(sum(ans))