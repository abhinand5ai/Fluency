from typing import List,Tuple
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def sort(a:ListNode) -> ListNode:
            if a.next is None:
                return a
            less = filter(a.next, lambda x: x.val < a.val)
            great = filter(a.next, lambda x: x.val >= a.val)
            a.next = None
            return concat(concat(less,a),great)

        
        def concat(a:ListNode, b:ListNode):
            if a is None:
                return b
            if b is None:
                return a
            c = ListNode(None,None)
            curr = c
            while a:
                curr.next = a
                a = a.next
                curr = curr.next
            curr.next = b
            c = c.next
            return c

        def filter(a:ListNode, func) -> ListNode:
            s = ListNode(None,None)
            start = s
            while a:
                if func(a):
                    start.next = ListNode(a.val, None)
                    start = start.next
                    a = a.next
            return start.next

        return sort(head)

    def print(self, head: ListNode):
        ls = []
        while head:
              ls.append(head.val)
              head = head.next
        print(" ".join([str(x) for x in ls]))

    def createLinkedList(self, ls: List[int]) -> ListNode:
        head = ListNode(None, None)
        curr = head
        for x in ls:
            curr.next =  ListNode(x, None)
            curr = curr.next
        return head.next 

if __name__ == "__main__":
    sol = Solution()
    #ls = sol.createLinkedList([4,2,1,3,5,7,6])#,1,8,5,7,6])
    ls = sol.createLinkedList([4,2,1])#,1,8,5,7,6])
    sol.print(sol.sortList(ls))
