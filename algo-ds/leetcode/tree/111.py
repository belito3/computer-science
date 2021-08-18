from binary_tree import TreeNode, printTree
from collections import deque


def minDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    if (root.left is not None) and (root.right is None):
        return 1 + minDepth(root.left)

    if (root.left is None) and (root.right is not None):
        return 1 + minDepth(root.right)
    return 1 + min(minDepth(root.left), minDepth(root.right))


def minDepthBFS(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    q = deque()
    q.append(root)
    layer = 1

    while q:
        for _ in range(len(q)):
            n = q.popleft()
            if node.left is None and node.right is None:
                return layer

            if node.left is not None:
                q.append(node.left)

            if node.right is not None:
                q.append(node.right)
        layer += 1
    return 0



