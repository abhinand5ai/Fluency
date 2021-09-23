# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        def height(node: TreeNode) -> int:
            if node is None:
                return 0
            return 1 + max(height(node.left), height(node.right))
        count = [0] * height(root)
        bin
