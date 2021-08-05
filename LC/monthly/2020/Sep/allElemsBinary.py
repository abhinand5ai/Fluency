# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list[int]:
        def ascending(node: TreeNode):
            if node is None:
                return
            yield from ascending(node.left)
            yield node.val
            yield from ascending(node.right)

        def inorderIterator(node: TreeNode):
            stack = []
            while node or stack:
                while node:
                    stack.append(node)
                    node = node.left
                node = stack.pop()
                yield node.val
                node = node.right

        order1 = inorderIterator(root1)
        order2 = inorderIterator(root2)
        mergedList = []
        stopReason = 0
        a, b = next(order1, None), next(order2, None)
        while a or b:
            if a is not None and (b is None or a <= b):
                mergedList.append(a)
                a = next(order1, None)
            else:
                mergedList.append(b)
                b = next(order2, None)
        return mergedList
