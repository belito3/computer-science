from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_minimal_tree(arr: List[int]) -> TreeNode:
    return create_tree_helper(arr, 0, len(arr)-1) 


def create_tree_helper(arr: List[int], left: int, right: int) -> TreeNode:
    # Time: O(N)
    # Space: O(N) for stack
    if left > right:
        return None
    mid = int((left + right)/2)
    node = TreeNode(val=arr[mid])

    node.right = create_tree_helper(arr, mid+1, right) 
    node.left = create_tree_helper(arr, left, mid-1)

    return node


def printTree(node: TreeNode):
    if node is None:
        return
    q = deque()
    m = set()

    q.append(node)
    m.add(node)

    while q:
        n = q.popleft()
        #print(n.val)
        print(f"{n.val} -> ", end="")
        if (n.left is not None) and (n.left not in m):
            q.append(n.left)
            m.add(n.left)

        if (n.right is not None) and (n.right not in m):
            q.append(n.right)
            m.add(n.right)

    print()


    
if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]

    node = create_minimal_tree(arr)
    printTree(node)

