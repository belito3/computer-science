from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildInCompleteTree(arr: List[int]) -> TreeNode:
    if len(arr) == 0:
        return None

    nodeQ = deque()
    valQ  = deque()

    for i in range(1, len(arr)):
        valQ.append(arr[i])

    root = TreeNode(val=arr[0])
    nodeQ.append(root)

    while valQ:
        left = valQ.popleft() if len(valQ) > 0 else None
        right = valQ.popleft() if len(valQ) > 0 else None

        node = nodeQ.popleft()
        #print(node.val)
        if left is not None:
            node.left = TreeNode(val=left)
            nodeQ.append(node.left)

        if right is not None:
            node.right = TreeNode(val=right)
            nodeQ.append(node.right)

    return root



def create_binary_tree(arr: []) -> TreeNode:
    # Apply with complete tree
    if len(arr) == 0:
        return None
    root = create_node(arr, 0, len(arr))
    return root

def create_node(arr, i, n):
    # Complete tree
    if i < n:
        node = TreeNode()
        if arr[i] is None:
            return None
        node = TreeNode(val=arr[i])
        node.left = create_node(arr, 2*i+1, n)
        node.right = create_node(arr, 2*i+2, n)
        return node
    return None


def printBinaryTree(node: TreeNode):
    q = deque()
    q.append(node)

    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node is not None:
                print(node.val, end="\t")
                q.append(node.left)
                q.append(node.right)
            else:
                print(node, end="\t")
        print()
    print()



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
        if n is not None:
            print(f"{n.val} -> ", end="")
            if n.left not in m:
                q.append(n.left)
                m.add(n.left)

            if n.right not in m:
                q.append(n.right)
                m.add(n.right)
        else:
            print("None ->")

    print()


if __name__ == "__main__":
    print("Test build a complete tree" )
    arr = [1,2,2,3,None,None,3,4,None,None,4]
    #root = create_binary_tree(arr)
    root = buildInCompleteTree(arr)
    printBinaryTree(root)


    print("Test build incomplete tree")
    arr = [5,4,8,11,None,17,4,7,None,None,None,5]
    root = buildInCompleteTree(arr=arr)
    printBinaryTree(root)
