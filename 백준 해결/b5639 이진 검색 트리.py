import sys
input = sys.stdin.readlines
sys.setrecursionlimit(10**6)

lines = input()

class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Graph:
    def __init__(self, val):
        self.root = Tree(val)

    def insert(self, val, cur=Tree(None)):
        while cur:
            if val < cur.val:
                if not cur.left:
                    cur.left = Tree(val)
                    return
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = Tree(val)
                    return
                cur = cur.right
            
    def postorder(self, cur=Tree(None)):
        if cur.left:
            self.postorder(cur.left)
        if cur.right:
            self.postorder(cur.right)
        print(cur.val)

graph = None

for line in lines:
    node = int(line)
    if not graph:
        graph = Graph(node)
    else:
        graph.insert(node, graph.root)

graph.postorder(graph.root)