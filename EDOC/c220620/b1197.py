import sys
input = sys.stdin.readline

V, E = map(int, input().split(' '))

edges = []
vertex = [v for v in range(V+1)]

for e in range(E):
    a, b, val = map(int, input().split(' '))
    edges.append([a, b, val])

edges.sort(key = lambda x:x[2])

def find(v):
    if vertex[v] == v:
        return v
    return find(vertex[v])

def union(a, b):
    a = find(a)
    b = find(b)
    if a<b:
        vertex[b] = a
    else:
        vertex[a] = b

selected = []
for a, b, val in edges:
    if len(selected) == V-1:
        break
    if find(a)!=find(b):
        union(a, b)
        selected.append(val)

print(sum(selected))