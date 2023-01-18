# 가르침 https://www.acmicpc.net/problem/1062
# 시간 초과 해결 못함

from itertools import combinations
import sys
input = sys.stdin.readline

N, K = map(int, input().split(' '))
letter = set()
words = list()

for n in range(N):
    temp = set(input().rstrip())-set(['a', 'n', 't', 'i', 'c']) # 단어 내 알파벳을 중복 제거하여 저장
    words.append(temp) # 단어 저장
    letter = letter.union(temp) # 모든 단어에 쓰인 알파벳만 저장

K-=5

if K<0:
    print(0)
    sys.exit(0)

answer = 0
for p in combinations(letter, K): # 모든 단어에 쓰인 알파벳을 K개로 조합
    cnt = 0
    for w in words:
        if w-set(p)==set(): # 단어가 조합된 알파벳만으로 이루어져있는지 확인
           cnt+=1
    if cnt>answer:
        answer=cnt
    if cnt==N:
        break

print(answer)
    