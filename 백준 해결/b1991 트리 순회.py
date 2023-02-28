import sys
input = sys.stdin.readline

N = int(input())

class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Graph:
    def __init__(self):
        self.root = Tree('A')

    def insert(self, p, l, r, cur=Tree('A')):
        if cur.value == p:
            cur.left = Tree(l)
            cur.right = Tree(r)
        else:
            if cur.left!=None:
                self.insert(p, l, r, cur.left)
            if cur.right!=None:
                self.insert(p, l, r, cur.right)
                
    
    def preorder(self, cur = Tree('A')):
        if cur.value!='.':
            print(cur.value, end='')
        if cur.left!=None:
            self.preorder(cur.left)
        if cur.right!=None:
            self.preorder(cur.right)
    
    def inorder(self, cur=Tree('A')):
        if cur.left!=None:
            self.inorder(cur.left)
        if cur.value!='.':
            print(cur.value, end='')
        if cur.right!=None:
            self.inorder(cur.right)
    
    def postorder(self, cur=Tree('A')):
        if cur.left!=None:
            self.postorder(cur.left)
        if cur.right!=None:
            self.postorder(cur.right)
        if cur.value!='.':
            print(cur.value, end='')

    
graph = Graph()

for n in range(N):
    p, l, r = map(str, input().strip().split(' '))
    graph.insert(p, l, r, graph.root)
    

graph.preorder(graph.root)
print()
graph.inorder(graph.root)
print()
graph.postorder(graph.root)