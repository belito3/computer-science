from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printTree(node: TreeNode):
    if node is None:
        return

    q = deque()
    m = set()

    q.append(node)
    m.add(node)

    while q:
        n = q.popleft()
        print(f"{n.val} ->", end="")
        if (n.left is not None) and (n.left not in m):
            q.append(n.left)
            m.add(n.left)

        if (n.right is not None) and (n.right not in m):
            q.append(n.right)
            m.add(n.right)

    print()



