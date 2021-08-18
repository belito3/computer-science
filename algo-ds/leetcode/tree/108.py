from typing import List, Optional
from binary_tree import TreeNode, printTree


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    return  BSTBalance(nums, 0, len(nums)-1) 

def BSTBalance(nums: List[int], start: int, end: int) -> Optional[TreeNode]:
    if start > end:
        return None

    mid = int((start+end)/2)
    node = TreeNode(val=arr[mid])

    node.left = BSTBalance(nums, start, mid-1)
    node.right = BSTBalance(nums, mid+1, end)

    return node 



