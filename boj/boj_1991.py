# Silver 1

import sys

class Node:
    def __init__(self, root, left_node, right_node):
        self.root = root
        self.left_node = left_node
        self.right_node = right_node
    
def preorder(node):
    print(node.root, end='')
    
    if node.left_node != ".":
        preorder(tree[node.left_node])
    
    if node.right_node != ".":
        preorder(tree[node.right_node])

def inorder(node):
    if node.left_node != ".":
        inorder(tree[node.left_node])
    
    print(node.root, end='')

    if node.right_node != ".":
        inorder(tree[node.right_node])

def postorder(node):
    if node.left_node != ".":
        postorder(tree[node.left_node])
    
    if node.right_node != ".":
        postorder(tree[node.right_node])
    
    print(node.root, end='')

# 노드 개수
n = int(input())

# 부모/자식 노드 관계 표현을 위한 딕셔너리
# ex) A(부모): [B, C](자식)
tree = {}

for i in range(n):
    root, left_node, right_node = input().split()
    
    tree[root] = Node(root, left_node, right_node)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])