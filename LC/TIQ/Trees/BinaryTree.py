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

    @staticmethod
    def in_order_traversal(node: TreeNode):
        if not (node.left is None):
            yield from TreeUtils.in_order_traversal(node.left)
        yield node.val
        if not (node.right is None):
            yield from TreeUtils.in_order_traversal(node.right)

    @staticmethod
    def is_valid_bst(root: TreeNode) -> bool:
        if root is None:
            return True
        prev, *traversal = TreeUtils.in_order_traversal(root)
        for i in traversal:
            if prev >= i:
                return False
            else:
                prev = i
        return True

    @staticmethod
    def is_symmetric(root: TreeNode) -> bool:
        if root is None:
            return True

        def right_in_order_traversal(node: TreeNode, x: int, y: int):
            if not (node.right is None):
                yield from right_in_order_traversal(node.right, x + 1, y + 1)
            yield node.val, x, y
            if not (node.left is None):
                yield from right_in_order_traversal(node.left, x - 1, y + 1)

        def in_order_traversal(node: TreeNode, x: int, y: int):
            if not (node.left is None):
                yield from in_order_traversal(node.left, x - 1, y + 1)
            yield node.val, x, y
            if not (node.right is None):
                yield from in_order_traversal(node.right, x + 1, y + 1)

        for right_first, left_first in zip(right_in_order_traversal(root, 0, 0), in_order_traversal(root, 0, 0)):
            if None in [right_first, left_first]:
                return False
            r_val, r_x, r_y = right_first
            l_val, l_x, l_y = left_first
            if r_val != l_val or r_x != -l_x or r_y != l_y:
                return False
        return True

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

    def test_inorder_tree(self):
        level_order_traversal: List[int] = [2, 1, 3, 1, 1]
        inorder: List[int] = [1, 1, 1, 2, 3]
        root: TreeNode = TreeUtils.construct_tree(level_order_traversal.copy())
        self.assertEqual(inorder, list(TreeUtils.in_order_traversal(root)))

    def test_valid_bst(self):
        level_order_traversal: List[int] = [1, 1]
        level_order_traversal_2: List[int] = [5, 1, 4, None, None, 3, 6]

        root: TreeNode = TreeUtils.construct_tree(level_order_traversal.copy())
        root2: TreeNode = TreeUtils.construct_tree(level_order_traversal_2.copy())

        self.assertTrue(TreeUtils.is_valid_bst(root))
        self.assertFalse(TreeUtils.is_valid_bst(root2))
