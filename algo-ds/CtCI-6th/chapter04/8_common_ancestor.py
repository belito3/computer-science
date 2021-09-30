from binary_tree import TreeNode, printBinaryTree, create_binary_tree


def first_common_ancestor(root: TreeNode, p1: TreeNode, p2: TreeNode) -> TreeNode:
    rs = find_node(root, p1, p2)
    return rs.node


class Result:
    def __init__(self):
        self.r1 = False
        self.r2 = False
        self.node = None


def find_node(root: TreeNode, p1: TreeNode, p2: TreeNode) -> Result:
    rs = Result()
    
    if root is None:
        return rs
    #print(p1.val, p2.val , root.val)
    if root.val == p1.val:
        rs.r1 =  True

    if root.val == p2.val:
        rs.r2 = True

    rs1 = find_node(root.left, p1, p2)
    rs2 = find_node(root.right, p1, p2)

    rs.r1 = rs.r1 or rs1.r1 or rs2.r1
    rs.r2 = rs.r2 or rs1.r2 or rs2.r2

    if rs1.node is not None:
        rs.node = rs1.node

    if rs2.node is not None:
        rs.node = rs2.node

    if rs.r1 and rs.r2 and (rs.node is None):

        rs.node = root
    return rs

if __name__ == "__main__":
    tree = [15, 7, 30, 4, 13, 20, 35, 3, 6, 10, 14, None, None, None, None]
    nodes = [(6, 10), (4, 6), (7, 6), (3, 7), (3, 14), (6, 35)]

    root = create_binary_tree(tree)
    printBinaryTree(root)
    for n in nodes:
        p1 = TreeNode(n[0])
        p2 = TreeNode(n[1])
        node_rs = first_common_ancestor(root, p1, p2)
        print(f"p1 = {n[0]}, p2 = {n[1]}, common = {node_rs.val}")
    

    
