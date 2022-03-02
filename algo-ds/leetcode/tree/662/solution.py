from typing import Optional, List
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
    valQ = deque()

    root = TreeNode(val=arr[0])
    nodeQ.append(root)

    for i in range(1, len(arr)):
        valQ.append(arr[i])


    while valQ:
        left = valQ.popleft() if valQ else None
        right = valQ.popleft() if valQ else None

        node = nodeQ.popleft()
        if left is not None:
            node.left = TreeNode(val=left)
            nodeQ.append(node.left)

        if right is not None:
            node.right = TreeNode(val=right)
            nodeQ.append(node.right)

    return root




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


from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((0, root))
        w = 0
        
        while q:    
            start = -1        
            for i in range(len(q)):
                index, node = q.popleft()
                if node is not None:
                    if start == -1:
                        start = index

                    w = max(w, index-start+1)

                    q.append((index*2, node.left))
                    q.append((index*2 + 1, node.right))
                
        return w

if __name__ == "__main__":
    input_ = [[0, 0, 0,
    None, 0, 0, None,
    None, 0, 0, None,
    None, 0, 0, None,
    None, 0, 0, None,
    None,0,0,None,
    None,0,0,None,
    None,0,0,None,
    None,0,0,None,
    None,0,0,None,
    None,0,0,None,
    None,0,0,None,
    None,0,0,None,
    None,0,0,None,
    None,0,0,None,
    None,0,0,None,
    None,0,0,None,
    None,0,0,None,
    None,0,0,None,
    None,0,0,None,
    None,0,0,None, # 22
    None,0,0,None,None,0,0,None,
    None,0,0,None,None,0,0,None,
    None,0,0,None,None,0,0,None,
    None,0,0,None,None,0,0,None,
    None,0,0,None,None,0,0,None,
    None,0,0,None,None,0,0,None,
    None,0,0,None,None,0,0,None,
    None,0,0,None,None,0,0,None,
    None,0,0,None,None,0,0,None,
    None,0,0,None,None,0,0,None,
    None,0,0,None,None,0,0,None,
    None,0,0,None,None,0,0,None,
    None,0,0,None,None,0,0,None,
    None,0,0,None,None,0,0,None,
    None,0,0,None,None,0,0,None,
    None,0,0,None,None,0,0,None,
    None,0,0,None,None,0,0,None,
    None,0,0,None,None,0,0,None,
    None,0,0,None,None,0,0,None,
    None,0,0,None,None,0,0,None,
    None,0,0,None,None,0,0,None,
    None,0,0,None,None,0,0,None,
    None,0,0,None,None,0,0,None, # 23 * 2
    None,0,0,None],
    [1,3,2,5,3,None,9],
    [1,3,None,5,3],
    [1,3,2,5]]
    for arr in input_:
        root = buildInCompleteTree(arr)
        # printBinaryTree(root)

        s = Solution()
        w = s.widthOfBinaryTree(root)
        print(w)

