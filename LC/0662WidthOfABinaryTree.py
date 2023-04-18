# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = [root]
        d = {}
        mx_width = 1

        def dfs(node, x, y):
            if node is None:
                return
            nonlocal mx_width
            mx, mn = d[x] if x in d and d[x] is not None else (None, None)
            mx = max(x, mx) if mx is not None else x
            mn = min(x, mn) if mn is not None else x
            d[x] = mx, mn
            mx_width = max(mx_width, mx - mn + 1)
            dfs(node.left, x + 1, y)
            dfs(node.right, x + 1, y + 1)

        dfs(root, 0, 0)
        return mx_width


