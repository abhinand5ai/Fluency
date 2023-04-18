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
        val_index = {}
        for i, v in enumerate(inorder):
            val_index[v] = i
        def buildTree(in_s, in_e, p_i):
            if in_e < in_s:
                return None
            if in_s == in_e:
                return TreeNode(inorder[in_s])
            val = preorder[p_i]

            loc = val_index[val]
            left_sub_size = loc - in_s + 1
            left = buildTree(in_s, loc - 1, p_i + 1)
            right = buildTree(loc + 1, in_e, p_i + left_sub_size)
            return TreeNode(val, left, right)
        return buildTree(0, len(inorder) - 1, 0)






def main():
    sol = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    tree = sol.buildTree(preorder, inorder)
    print(tree)


if __name__ == '__main__':
    main()
