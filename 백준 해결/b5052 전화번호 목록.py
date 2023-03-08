import sys
input = sys.stdin.readline

T = int(input())

class Tree:
    def __init__(self, value):
        self.value = value
        self.children = [None]*10

class Graph:
    def __init__(self):
        self.root = Tree(0)

for t in range(T):
    N = int(input())
    phone_num = [input().rstrip() for n in range(N)]
    phone_num.sort()

    graph = Graph()
    ans = True

    for ph in phone_num:
        if not ans:
            break
        cur = graph.root
        flag = True
        for s in ph:
            if cur!=graph.root and flag and cur.children.count(None)==10:
                ans = False
                break
            if not cur.children[int(s)]:
                cur.children[int(s)] = Tree(int(s))
                flag = False
            cur = cur.children[int(s)]
    
    if ans:
        print("YES")
    else:
        print("NO")
            
