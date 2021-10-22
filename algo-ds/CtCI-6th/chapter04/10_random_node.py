from typing import Optional
from collections import deque

from binary_tree import printBinaryTree


class BinaryTreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val) -> None:
        if self.val is None:
            self.val = val
            return

        # find node None
        q = deque()
        q.append(self)
        while True:
            for _ in range(len(q)):
                n = q.popleft()
                if n.left is None:
                    n.left = BinaryTreeNode(val=val)
                    return

                if n.right is None:
                    n.right = BinaryTreeNode(val=val)
                    return
                q.append(n.left)
                q.append(n.right)



    def find(self, val):
        return find_helper(root, val)

    def delete(self, val):
        pass

    def randomNode(self):
        pass

def find_helper(root, val):
    if root is None:
        return None

    if root.val == val:
        return root

    left = find_helper(root.left, val)
    right = find_helper(root.right, val)

    if left is not None:
        return left
    if right is not None:
        return right
    return None


if __name__ == "__main__":
    root = BinaryTreeNode()
    arr = [1,2,3,4,5]
    for a in arr:
        root.insert(a)
    printBinaryTree(root)

    root.insert(6)
    root.insert(7)
    printBinaryTree(root)

    print(root.find(1).val)
    print(root.find(5).val)
    print(root.find(10))




