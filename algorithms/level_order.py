"""
Level order traversal in a tree is equivalent to BFS in a graph.

Recursive implementation:
Time Complexity: O(n^2) in worst case. For a skewed tree, printGivenLevel() takes O(n) time where n is the number of
nodes in the skewed tree. So time complexity of printLevelOrder() is O(n) + O(n-1) + O(n-2) + .. + O(1) which is O(n^2).
Auxiliary Space:  O(n) in the worst case. For a skewed tree, printGivenLevel() uses O(n) space for call stack. For a
Balanced tree, the call stack uses O(log n) space, (i.e., the height of the balanced tree).

Iterative implementation:
Time Complexity: O(n) where n is the number of nodes in the binary tree
Auxiliary Space: O(n) where n is the number of nodes in the binary tree
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

    def insert(self, val):
        new_node = Node(val)
        if not self.root:
            self.root = new_node
            return
        temp = self.root
        prev = None
        while temp:
            prev = temp
            if temp.val < val:
                temp = temp.right
            else:
                temp = temp.left
        if prev.val < val:
            prev.right = new_node
        else:
            prev.left = new_node

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.val, end=' ')
        self.inorder(root.right)

    def level_order_iterative(self):
        if not self.root:
            return
        queue = deque()
        queue.append(self.root)
        while queue:
            for i in range(0, len(queue)):
                curr = queue.popleft()
                print(curr.val, end=' ')
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

    def level_order_recursive(self):
        temp = self.root
        height = self.height(temp)
        for i in range(1, height+1):
            self.print_current_level(temp, i)

    def height(self, root):
        if not root:
            return 0
        else:
            l_height = self.height(root.left)
            r_height = self.height(root.right)
            if l_height > r_height:
                return l_height+1
            else:
                return r_height+1

    def print_current_level(self, root, h):
        if not root:
            return
        if h == 1:
            print(root.val, end=' ')
        elif h > 1:
            self.print_current_level(root.left, h-1)
            self.print_current_level(root.right, h-1)


def main():
    tree = Tree()
    values = [6, 4, 7, 3, 5, 9, 2, 8, 10]
    for value in values:
        tree.insert(value)
    print('In order:')
    tree.inorder(tree.root)
    print('\nLevel order iterative:')
    tree.level_order_iterative()
    print('\nLevel order recursive:')
    tree.level_order_recursive()


if __name__ == "__main__":
    main()
