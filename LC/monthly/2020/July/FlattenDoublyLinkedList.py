# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def rflatten(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        if head.next is None and head.child is None:
            return head                                                                                                                                                                                         
        if head.child is None:
            return self.rflatten(head.next)
        else:
            head.child.prev =  head
            child = self.rflatten(head.child)
            child.next = head.next
            if head.next is not None:
                head.next.prev = child
            head.next = head.child
            head.child = None
            return self.rflatten(child.next)

    def flatten(self, head:'Node') -> 'Node':
        tail = self.rflatten(head)
        if tail is None:
            return None
        while tail.prev is not None:
            tail = tail.prev
        return tail