import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

def insert(parent, left, right, BST=Tree(None)):
    if BST.value == parent:
        BST.left = Tree(left)
        BST.right = Tree(right)
        return
    if BST.left:
        insert(parent, left, right, BST.left)
    if BST.right:
        insert(parent, left, right, BST.right)

BST = Tree('A')
N = int(input())
for n in range(N):
    parent, left, right = map(str, input().split(' '))
    insert(parent, left, right, BST)
    