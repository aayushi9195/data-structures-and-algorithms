"""
Binary Search Tree.

Time complexity:
https://www.geeksforgeeks.org/complexity-different-operations-binary-tree-binary-search-tree-avl-tree/

OPERATION	WORST CASE	AVERAGE CASE	BEST CASE	SPACE
Search	           O(N)	     O(logN)	    O(1)	O(N)
Insert	           O(N)	     O(logN)	    O(1)	O(N)
Delete	           O(N)	     O(logN)	    O(N)	O(N)
"""
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def search(self, val):
        if not self.root:
            print("Tree is empty")
            return
        temp = self.root
        while temp:
            if temp.val == val:
                return True
            if temp.val < val:
                temp = temp.right
            else:
                temp = temp.left
        return False

    def insert(self, val):
        new_node = Node(val)
        if not self.root:
            self.root = new_node
            return
        curr = self.root
        prev = None
        while curr:
            prev = curr
            if curr.val < val:
                curr = curr.right
            else:
                curr = curr.left
        if prev.val < val:
            prev.right = new_node
        else:
            prev.left = new_node

    def delete(self, root, val):
        if not root:
            return None
        if root.val == val:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            if root.left and root.right:
                temp = root.right
                while temp.left:
                    temp = temp.left
                root.val = temp.val
                root.right = self.delete(root.right, root.val)
        elif root.val > val:
            root.left = self.delete(root.left, val)
        else:
            root.right = self.delete(root.right, val)
        return root

    def preorder(self, node):
        if not node:
            return
        print(node.val, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self, node):
        if not node:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.val, end=" ")

    def inorder_recursive(self, node):
        if not node:
            return
        self.inorder_recursive(node.left)
        print(node.val, end=" ")
        self.inorder_recursive(node.right)

    def inorder_iterative(self):
        if not self.root:
            return []
        curr = self.root
        stack = deque()
        ans = []
        stack.append(curr)
        while stack:
            while curr.left:
                stack.append(curr.left)
                curr = curr.left
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                curr = node.right
                stack.append(curr)
        print(ans)


def main():
    tree = Tree()
    tree.insert(6)
    tree.insert(4)
    tree.insert(7)
    tree.insert(3)
    tree.insert(5)
    tree.insert(9)
    tree.insert(2)
    tree.insert(8)
    tree.insert(10)
    tree.preorder(tree.root)
    print('\n')
    tree.postorder(tree.root)
    print('\n')
    tree.inorder_recursive(tree.root)
    print('\n')
    tree.inorder_iterative()
    print(tree.search(2))
    print(tree.search(5))
    print(tree.search(8))
    print(tree.search(10))
    print(tree.search(14))
    root = tree.delete(tree.root, 10)
    root = tree.delete(root, 7)
    root = tree.delete(root, 3)
    root = tree.delete(root, 4)
    root = tree.delete(root, 6)
    tree.inorder_recursive(root)


if __name__ == "__main__":
    main()