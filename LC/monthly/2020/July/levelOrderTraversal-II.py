# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Traversal:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        traversal = [[root]]
        currLvl = traversal[-1]
        while currLvl:
            nextLvl = []
            for child in currLvl:
                nextLvl.append(child.left)
                nextLvl.append(child.right)
            currLvl = [x for x in  nextLvl if x is not None]
            traversal.append(currLvl)
        traversal.reverse()
        return traversal
