class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = 0
        curr = head
        while curr:
            curr = curr.next
            l += 1

        groups = l // k
        if head is None:
            return Nonew
        c_head = head
        ret = None
        prev_tail = None
        while groups:
            curr, next = c_head, c_head.next
            i = k
            while next and i > 1:
                tmp = next.next
                next.next = curr
                curr = next
                next = tmp
                i -= 1
            ret = curr if ret is None else ret
            if prev_tail:
                prev_tail.next = curr
            prev_tail = c_head
            c_head.next = next
            c_head = c_head.next
            groups -= 1

        return ret
