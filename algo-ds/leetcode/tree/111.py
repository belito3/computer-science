from binary_tree import TreeNode, printTree


def minDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    if (root.left is not None) and (root.right is None):
        return 1 + minDepth(root.left)

    if (root.left is None) and (root.right is not None):
        return 1 + minDepth(root.right)
    return 1 + min(minDepth(root.left), minDepth(root.right))

