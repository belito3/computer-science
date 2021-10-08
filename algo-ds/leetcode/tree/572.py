from collections import deque

from binary_tree import TreeNode, create_binary_tree, printBinaryTree

def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
    nodes = find_root_common(root, subRoot)
    for _ in range(len(nodes)):
        node = nodes.popleft()
        if compare_tree(node, subRoot):
            return True
    return False


def compare_tree(root1: TreeNode, root2: TreeNode) -> bool:
    q1 = deque()
    q2 = deque()
    
    q1.append(root1)
    q2.append(root2)

    while q1 or q2:
        if len(q1) != len(q2):
            return False
        for _ in range(len(q1)):
            n1 = q1.popleft()
            n2 = q2.popleft()
            
            if (n1 is None) or (n2 is None):
                if n1 == n2: # (=None)
                    continue
                return False
                
            if n1.val != n2.val:
                return False
            
            if n1 is not None:
                q1.append(n1.left)
                q1.append(n1.right)
                
            if n2 is not None:
                q2.append(n2.left)
                q2.append(n2.right)
    return True

def find_root_common(root: TreeNode, subRoot: TreeNode):
    q = deque()
    rs = deque()

    q.append(root)
    
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node is None:
                continue

            if node.val == subRoot.val:
                rs.append(node)

            q.append(node.left)
            q.append(node.right)

    return rs


if __name__ == "__main__":
    trees = [[3,4,5,1,2],[4,1,2], [3,4,5,1,2,None,None,None,None,0], [4,1,2]]

    for i in range(0, len(trees), 2):
        tree = create_binary_tree(trees[i])
        subtree = create_binary_tree(trees[i+1])

        printBinaryTree(tree)
        printBinaryTree(subtree)
        print(f"rs = {isSubtree(tree, subtree)}")

    
