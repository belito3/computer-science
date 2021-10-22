from binary_tree import TreeNode, printBinaryTree, create_binary_tree

def num_path_with_sum(root: TreeNode, target):
    cnt, acc = sum_node(root, target)
    return cnt


def sum_node(root: TreeNode, target):
    # return rs, accumulation
    if root is None:
        return 0, []

    rs_left, acc_left = sum_node(root.left, target)
    rs_right, acc_right = sum_node(root.right, target)

    sum_left = [a + root.val for a in acc_left]
    sum_right = [a + root.val for a in acc_right]
    acc = [root.val] + sum_left + sum_right

    cnt = 0
    for a in acc:
        if a == target:
            cnt += 1

    rs = rs_left + rs_right + cnt

    return rs, acc


if __name__ == "__main__":
    arr = [10, 5, -3, 3, 2, None, 11]
    arr = [10, 5, -3]
    target = 0
    root = create_binary_tree(arr)
    cnt = num_path_with_sum(root, target)
    print(cnt)

    print(sum_node(root, target)[0])
