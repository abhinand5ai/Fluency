# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        a_head = head
        b_head =  head.next
        a, b = head, head.next
        while b:
            a.next = b.next
            a = a.next
            if b.next:
                b.next = b.next.next
                b = b.next

        
