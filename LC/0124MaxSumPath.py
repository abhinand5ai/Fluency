# Definition for a binary tree node.
from optparse import Option
from tkinter.tix import Tree
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxPath(node: Optional[TreeNode]):
            if node is None:
                return float('-inf'), float('-inf')
            mxUL, mxPL = maxPath(node.left)
            mxUR, mxPR = maxPath(node.right)
            maxUp = node.val + max(mxUL, mxUR, 0)
            maxP = max(mxPL, mxPR, node.val +
                       max(0, mxUL) + max(mxUR, 0), maxUp)
            return maxUp, maxP
        return maxPath(root)[1]
