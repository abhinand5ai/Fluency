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
        def set_children(node: TreeNode, traversal: List):
            if not traversal:
                return
            node.left = traversal.pop(0) if traversal[0] is None else TreeNode(traversal.pop(0))
            if not traversal:
                return
            node.right = traversal.pop(0) if traversal[0] is None else TreeNode(traversal.pop(0))

        def get_after_setting_children(nodes: List[TreeNode], traversal: List) -> List[TreeNode]:
            non_null_nodes = [node for node in nodes if node is not None]
            children_list: List[TreeNode] = []
            for node in non_null_nodes:
                set_children(node, traversal)
                children_list.append(node.left)
                children_list.append(node.right)
            return children_list

        if not level_order_traversal:
            return None
        root: TreeNode = TreeNode(level_order_traversal.pop(0))
        nodes: List[TreeNode] = [root]
        while True:
            if not level_order_traversal:
                return root
            nodes = get_after_setting_children(nodes, level_order_traversal)

    @staticmethod
    def bfs(root: TreeNode) -> List:
        node_list: List[TreeNode] = [root]
        level_order_traversal = []
        while node_list:
            next_level: List[TreeNode] = []
            for node in node_list:
                if node is not None:
                    level_order_traversal.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)
                else:
                    level_order_traversal.append(None)
            node_list = next_level
        while level_order_traversal and level_order_traversal[-1] is None:
            level_order_traversal.pop()
        return level_order_traversal


class Solution(object):
    def max_depth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return 1 + max(self.max_depth(root.left), self.max_depth(root.right))


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()

    def test_construct_tree(self):
        level_order_traversal: List[int] = [5, 1, 4, None, None, 3, 6]
        root: TreeNode = TreeUtils.construct_tree(level_order_traversal.copy())
        self.assertEqual(level_order_traversal, TreeUtils.bfs(root))
