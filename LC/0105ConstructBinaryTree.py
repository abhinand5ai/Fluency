# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val}, {self.left}, {self.right})"


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        pIndex = [0]

        def build(start, end):
            if start > end:
                return None
            if start == end:
                tree = TreeNode(preorder[pIndex[0]])
                pIndex[0] += 1
                return tree

            nodeLoc = inorder.index(preorder[pIndex[0]])
            tree = TreeNode(preorder[pIndex[0]])
            pIndex[0] += 1
            tree.left = build(start, nodeLoc - 1)
            tree.right = build(nodeLoc + 1, end)
            return tree

        return build(0, len(inorder) - 1)


def main():
    sol = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    tree = sol.buildTree(preorder, inorder)
    print(tree)


if __name__ == '__main__':
    main()
