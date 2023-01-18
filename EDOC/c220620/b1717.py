import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int, input().split(' '))
set_list = list()

for n in range(N+1):
    set_list.append(n)

def Find(a):
    if set_list[a] == a:
        return a
    set_list[a] = Find(set_list[a])
    return set_list[a]

def Union(a, b):
    a = Find(a)
    b = Find(b)
    if a!=b:
        if a < b:
            set_list[b] = a
        else:
            set_list[a] = b

for m in range(M):
    op, a, b = map(int, input().split(' '))
    if op == 0:
        Union(a, b)
    elif op == 1:
        if Find(a) == Find(b):
            print("YES")
        else:
            print("NO")