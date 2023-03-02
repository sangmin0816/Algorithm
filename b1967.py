#https://www.acmicpc.net/problem/1967

import sys
input = sys.stdin.readline

N = int(input())

class Tree:
    def __init__(self, num, distance):
        self.num = num
        self.left = None
        self.right = None
        self.distance = distance

class Graph:
    def __init__(self):
        self.root = Tree(1, 0)

    def insert(self, p, c, v, cur=Tree(1, 0)):
        if cur.num == p:
            if not cur.left:
                cur.left = Tree(c, v)
            else:
                cur.right = Tree(c, v)
        else:
            if cur.left:
                self.insert(p, c, v, cur.left)
            if cur.right:
                self.insert(p, c, v, cur.right)


graph = Graph()

for i in range(N-1):
    p, c, v = map(int, input().split(' '))
    graph.insert(p, c, v, graph.root)

