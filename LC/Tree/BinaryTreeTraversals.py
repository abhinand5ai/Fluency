from TreeNode import TreeNode
from typing import Optional


def preOrderRecursive(node: TreeNode) -> list[TreeNode]:
    traversal = []

    def preOrder(node: TreeNode):
        traversal.append(node.val)
        preOrder(node.left)
        preOrder(node.right)

    return traversal


def preorderStack(node: TreeNode) -> list[TreeNode]:
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


def inorderRecursive(node: TreeNode) -> list[TreeNode]:
    traversal = []

    def inorder(node: TreeNode):
        if node is None:
            return
        inorder(node.left)
        traversal.append(node)
        inorder(node.right)

    inorder(node)
    return traversal


def inorderStack(node: TreeNode) -> list[TreeNode]:
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


def postOrderRecursive(node: TreeNode) -> list[TreeNode]:
    traversal = []

    def postOrder(node: TreeNode):
        if node is None:
            return
        postOrder(node.left)
        postOrder(node.right)
        traversal.append(node)

    postOrder(node)
    return traversal


def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
    traversal = []
    stk = [(root, 0)]
    while stk:
        curr, dr = stk.pop()
        if curr is None:
            continue
        if dr == 0:
            stk.append((curr, 1))
            stk.append((curr.left, 0))
        elif dr == 1:
            stk.append((curr, 2))
            stk.append((curr.right, 0))
        elif dr == 2:
            traversal.append(curr.val)
    return traversal
