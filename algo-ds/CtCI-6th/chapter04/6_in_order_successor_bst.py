from typing import Optional

from binary_tree import TreeNode, printTree, printBinaryTree, create_binary_tree

def inOrderSuccessor(root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
    curr = root
    pre = None

    while curr is not None:
        if curr.val > p.val:
            pre = curr
            curr = curr.left
        else:
            curr = curr.right

    return pre


if __name__ == "__main__":
    arr = [7, 4, 10, 2, 6, 8, 12, None, None, 5, None]
    root = create_binary_tree(arr)
    printBinaryTree(root)
    _input = [4, 5, 8, 12]
    for i in _input:
        p = TreeNode(val=i)
        rs = inOrderSuccessor(root, p)
        num = rs.val if rs is not None else rs
        print(f"input = {i}, next = {num}")
