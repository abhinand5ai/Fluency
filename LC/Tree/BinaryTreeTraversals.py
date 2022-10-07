from TreeNode import TreeNode
from typing import List


class Traversals:
    def preOrderRecursive(node: TreeNode) -> List[TreeNode]:
        traversal = []

        def preOrder(node: TreeNode):
            traversal.append(node.val)
            preOrder(node.left)
            preOrder(node.right)
        return traversal

    def preorderStack(node: TreeNode) -> List[TreeNode]:
        traversal = []
        stk = [node]
        while stk:
            curr = stk.pop()
            if curr is None:
                continue
            traversal.append(curr)
            stk.append(curr.right)
            stk.append(curr.left)
        return traversal

    def inorderRecursive(node: TreeNode) -> List[TreeNode]:
        traversal = []

        def inorder(node: TreeNode):
            if node is None:
                return
            inorder(node.left)
            traversal.append(node)
            inorder(node.right)
        inorder(node)
        return traversal

    def inorderStack(node: TreeNode) -> List[TreeNode]:
        if node is None:
            return []
        traversal = []
        stk = [node]
        while stk:
            curr = stk.pop()
            if curr is None:
                curr = stk.pop()
                traversal.append(curr.val)
                stk.append(curr.right)
                continue
            stk.append(curr)
            stk.append(curr.left)
        return traversal

    def postOrderRecursive(node: TreeNode) -> List[TreeNode]:
        traversal = []

        def postOrder(node: TreeNode):
            if node is None:
                return
            postOrder(node.left)
            postOrder(node.right)
            traversal.append(node)

    def postorderStack(node: TreeNode) -> List[TreeNode]:
        traversal = []
        stk = [node]
        while stk:
            curr = stk.pop()
            if curr is None:
                pass
            #TODO

        return traversal
