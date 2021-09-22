from typing import List, Optional
import sys

from binary_tree import create_binary_tree, printTree, TreeNode

MAX_INT = INVALID_LEFT = sys.maxsize
MIN_INT = INVALID_RIGHT = - sys.maxsize - 1


class Value:
    def __init__(self, vmax=MIN_INT, vmin=MAX_INT):
        self.vmax = vmax
        self.vmin = vmin


def is_bst1(root: Optional[TreeNode]) -> bool:
    # BST: max(subtree_left) < root.value < min(subtree_right)
    v = get_value(root) 
    #print(f"v.max={v.vmax}, v.right={v.vmin}")
    if (v.vmax == MAX_INT) or (v.vmin == MIN_INT):
        return False
    return True


def get_value(root: Optional[TreeNode]) -> Value:
    v = Value()
    if root is None:
        return v

    v_left = get_value(root.left)
    if v_left.vmax == MAX_INT:
        v.vmax = MAX_INT
        return v

    v_right = get_value(root.right)
    if v_right.vmin == MIN_INT:
        v.vmin = MIN_INT
        return v

    if (v_left.vmax >= root.val) or (v_right.vmin <= root.val):
        v.vmax = MAX_INT
        return v

    v.vmax = max(root.val, v_left.vmax, v_right.vmax)
    v.vmin = min(root.val, v_left.vmin, v_right.vmin)
    return v

def is_bst(root: Optional[TreeNode]) -> bool:
    valid = check_bst(root, None, None)
    return valid

def check_bst(n: TreeNode, _min: int, _max: int) -> bool:
    if n is None:
        return True

    if _min is not None and n.val <= _min:
        return False

    if _max is not None and n.val > _max:
        return False

    if not check_bst(n.left, _min, n.val):
        return False

    if not check_bst(n.right, n.val, _max):
        return False

    #if ((_min is not None) and (n.val <= _min)) or ((_max is not None) and (n.val  > _max)):
    #    print(f"condition1 node: {n.val}")
    #    return False

    #if (not check_bst(n.left, _min, n.val)) or (not check_bst(n.right, n.val, _max)):
    #    print(f"condition2 node: {n.val}")
    #    return False
    return True

if __name__ == "__main__":
    arr = [[2,1,3],[5,1,4,None,None,3,6],[8,4,10,2,6,None,20], [8,4,10,2,12,None,20]]
    for a in arr:
        root = create_binary_tree(a)
        print(f"root val: {root.val}")
        printTree(root)
        rs = is_bst(root)
        print(f"is_bst: {rs}")
