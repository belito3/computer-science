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
        q.append(root)
        w = 0
        while q:
            cnt = 0
            null = 0
            has_not_null = False
            for i in range(len(q)):
                node = q.popleft()
                if node is not None:
                    has_not_null = True
                    cnt += 1 + null
                    null = 0
                else:
                    if has_not_null:
                        null += 1
                        q.append(None)
                        q.append(None)


                if node is not None:
                    q.append(node.left)
                    q.append(node.right)
            print(w)
            w = max(w, cnt)
        return w

if __name__ == "__main__":
    arr = [0, 0, 0,
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
    None,0,0,None,
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
    None,0,0,None,None,0,0,None,
    None,0,0,None]

    root = buildInCompleteTree(arr)
    printBinaryTree(root)

    s = Solution()
    w = s.widthOfBinaryTree(root)
    print(w)

