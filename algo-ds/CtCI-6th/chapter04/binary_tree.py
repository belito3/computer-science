from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(arr: []) -> TreeNode:
    if len(arr) == 0:
        return None
    node = TreeNode()  
    root = create_node(node, arr, 0, len(arr))
    return root

def create_node(node, arr, i, n):
    if i < n:
        node = TreeNode(val=arr[i])
        node.left = create_node(node.left, arr, 2*i+1, n)
        node.right = create_node(node.right, arr, 2*i+2, n)
    return node 
    

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
        print(f"{n.val} -> ", end="")
        if (n.left is not None) and (n.left not in m):
            q.append(n.left)
            m.add(n.left)

        if (n.right is not None) and (n.right not in m):
            q.append(n.right)
            m.add(n.right)

    print()


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    root = create_binary_tree(arr)
    printTree(root)
