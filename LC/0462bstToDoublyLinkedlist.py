"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        curr = root
        head = Node()
        dll = head
        while curr:
            if curr.left:
                right_most = curr.left
                while right_most.right:
                    right_most = right_most.right
                right_most.right = curr
                tmp = curr.left
                curr.left = None
                curr = tmp
            else:
                dll.right = curr
                dll = dll.right
                curr = curr.right

        curr = head.right
        while curr.right:
            curr.right.left = curr
            curr = curr.right
        curr.right = head.right
        tmp = head.right
        tmp.left = curr
        head.right = None
        return tmp
        

