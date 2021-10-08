from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_binary_tree(arr: []) -> TreeNode:
    if len(arr) == 0:
        return None
    root = create_node(arr, 0, len(arr))
    return root


def create_node(arr, i, n):
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
        print(f"{n.val} ->", end="")
        if (n.left is not None) and (n.left not in m):
            q.append(n.left)
            m.add(n.left)

        if (n.right is not None) and (n.right not in m):
            q.append(n.right)
            m.add(n.right)

    print()



