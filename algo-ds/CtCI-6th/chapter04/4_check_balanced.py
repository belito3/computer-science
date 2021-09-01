from typing import List
from collections import deque

from binary_tree import printTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 0


def create_binary_tree(arr:  List[int]) -> TreeNode:
    if len(arr) == 0:
        return None
    root = create_node(arr, 0, len(arr))
    return root
    

def create_node(arr: List[int], i: int, n: int) -> TreeNode:
    if i < n:
        if arr[i] is None:
            return None
        node = TreeNode(val=arr[i])
        node.left = create_node(arr, 2*i+1, n)
        node.right = create_node(arr, 2*i+2, n)
        return node
    return None


def check_balanced(node: TreeNode) -> bool:
    # Time: O(n)
    # Space: O(n) - used by stack
    if node is None:
        return True

    cal_height(node)
    q = deque()
    q.append(node)

    while q:
        for _ in range(len(q)):
            n = q.popleft()
            print(f"n={n.val}, height={n.height}")
            left = convert_height(n.left)
            right = convert_height(n.right)

            if abs(left - right) > 1:
                return False
            if n.left is not None:
                q.append(n.left)
            if n.right is not None:
                q.append(n.right)

    return True


def convert_height(node):
    if node is None:
        return -1
    return node.height


def cal_height(node: TreeNode):
    if node is None:
        return 0

    if (node.left is None) and (node.right is None):
        node.height = 0
        return 0
    node.height = 1 + max(cal_height(node.left), cal_height(node.right))
    return node.height


if __name__ == "__main__":
    arr = [[1,2,3,4], [1,2,3,None,None,4,5], [3,9,20,None,None,15,7], [1,2,2,3,3,None,None,4,4], [1,2,2,3,None,None,3,4,None,None,4]]
    for a in arr:
        node = create_binary_tree(a)
        printTree(node)
        print(f"balance: {check_balanced(node)}")
