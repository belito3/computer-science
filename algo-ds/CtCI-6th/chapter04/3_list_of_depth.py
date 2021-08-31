from typing import List
from collections import deque

from binary_tree import create_binary_tree, TreeNode

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def list_depths(root: TreeNode) -> List[ListNode]:
    # Time: O(n)
    # Space: O(n)
    if root is None:
        return []

    q = deque()
    q.append(root)
    list_node = [] 
    while q:
        dummy = l_node = ListNode()
        for _ in range(len(q)):
            node = q.popleft()
            if node is not None:
                l_node.next = ListNode(node.val)
                l_node = l_node.next
                q.append(node.left)
                q.append(node.right)
        list_node.append(dummy.next)
        # next layer

    return list_node


def printLinkedList(node: ListNode):
    while node is not None:
        print(node.val, end="->")
        node = node.next

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    root = create_binary_tree(arr)
    list_node = list_depths(root)
    for ll in list_node:
        printLinkedList(ll)
        print()
