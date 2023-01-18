import sys
input = sys.stdin.readline

from itertools import combinations

L, C = map(int, input().split(' '))
letters = list(map(str, input().strip().split(' ')))
vowels = set(['a', 'e', 'i', 'o', 'u']).intersection(letters)
consonants = set(letters) - set(['a', 'e', 'i', 'o', 'u'])


letters.sort()

ans = set()

for i in combinations(letters, L):
    if len(set(list(i)).intersection(vowels)) and len(set(list(i)).intersection(consonants))>=2:
        ans.add(''.join(i))

for a in sorted(list(ans)):
    print(a)