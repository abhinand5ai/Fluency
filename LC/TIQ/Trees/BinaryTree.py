# Definition for a binary tree node.
import unittest
from typing import List, Optional, Tuple


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeUtils:
    @staticmethod
    def construct_tree(level_order_traversal: List) -> Optional[TreeNode]:
            pass

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()
