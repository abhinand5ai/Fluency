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
                return 0
            mxUL, mxPL = maxPath(node.left)
            mxUR, mxPR = maxPath(node.right)
            maxUp = max(node.val + max(mxUL, mxUL), node.val)
            maxP = max(mxPL, mxPR, node.val + mxUL + mxUR, maxUp)
            return maxUp, maxP
        return maxPath(root)[1]
