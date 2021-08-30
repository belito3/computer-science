from typing import Optional, List
from collections import deque

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]
    rs = []
    if root is None:
        return rs

    q = deque()
    q.append(root)

    while q:
        l = []
        for _ in range(len(q)):
            node = q.popleft()
            if node is not None:
                l.append(node.val)
                q.append(node.left)
                q.apeend(node.right)
        if len(l) > 0:
            rs.append(l)

    return rs



