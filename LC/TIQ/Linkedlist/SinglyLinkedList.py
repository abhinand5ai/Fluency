import unittest
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        return

    def lenLinkedList(self, node: ListNode):
        if node is None:
            return 0
        else:
            return 1 + self.lenLinkedList(node.next)

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        return self.removeNthFromBeginning(head, self.lenLinkedList(head) - n)

    def removeNthFromEnd2(self, head, n):
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.val = node.val
            return i

        index(head)
        return head.next

    def removeNthFromBeginning(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return head
        if n == 0:
            return head.next
        else:
            head.next = self.removeNthFromBeginning(head.next, n - 1)
        return head

    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        prev: ListNode = None
        curr_node: ListNode = head
        next_node: ListNode = head.next
        while True:
            if next_node.next is None:
                next_node.next = curr_node
                curr_node.next = prev
                return next_node
            curr_node.next = prev
            prev, curr_node = curr_node, next_node
            next_node = next_node.next

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None or l2 is None:
            return l2 if l1 is None else l2

        merged_head: ListNode = None
        merge_point: ListNode = None
        if l1.val <= l2.val:
            merged_head = l1
            l1 = l1.next
        else:
            merged_head = l2
            l2 = l2.next
        merge_point = merged_head
        while True:
            if None in (l1, l2):
                merge_point.next = l1 or l2
                break
            elif l1.val <= l2.val:
                merge_point.next = l1
                merge_point = merge_point.next
                l1 = l1.next
            else:
                merge_point.next = l2
                merge_point = merge_point.next
                l2 = l2.next
        return merged_head

    def isPalindrome(self, head: ListNode) -> bool:
        n: int = self.lenLinkedList(head)
        if n == 1 or n == 0:
            return True
        if n % 2 == 0:
            second_half = self.split(head, int(n / 2))
            reversed_half = self.reverseList(second_half)
            is_palindrome = self.isEqual(head, reversed_half)
            self.concat(head, self.reverseList(reversed_half))
        else:
            middle = self.split(head, int(n / 2))
            second_half = self.split(middle, 1)
            reversed_half = self.reverseList(second_half)
            is_palindrome = self.isEqual(head, reversed_half)
            self.concat(middle, self.reverseList(reversed_half))
            self.concat(head, middle)
        return is_palindrome

    def isEqual(self, l1: ListNode, l2: ListNode):
        if l1 is l2:
            return True
        elif l1 is None or l2 is None:
            return False
        elif l1.val == l2.val:
            return self.isEqual(l1.next, l2.next)

    def split(self, l: ListNode, n: int) -> ListNode:
        if n <= 0 or l is None:
            return l
        elif n == 1:
            ret = l.next
            l.next = None
            return ret
        else:
            return self.split(l.next, n - 1)

    def concat(self, l1: ListNode, l2: ListNode):
        if l1 is None or l2 is None:
            return l2 if l1 is None else l2
        elif l1.next is None:
            l1.next = l2
        else:
            self.concat(l1.next, l2)


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()

    def load_linked_list(self, list: List[ListNode]) -> ListNode:
        if len(list) == 0 or list is None:
            return None

        node: ListNode = ListNode(list[0])
        tmp = node
        for val in list[1:]:
            tmp.next = ListNode(val)
            tmp = tmp.next

        return node

    def load_list_from_linked_list(self, node: ListNode) -> List:
        linked_list: List = []
        while True:
            if node is None:
                return linked_list
            else:
                linked_list.append(node.val)
                node = node.next

        return linked_list

    def test_is_palindrome(self):
        l: List = [1, 0, 1]
        linked_list: ListNode = self.load_linked_list(l)
        self.assertTrue(self.sol.isPalindrome(linked_list))

    def test_merge_sorted_list(self):
        linked_list1: List = [1, 1, 2, 3, 4, 5]
        linked_list2: List = [1, 2, 3, 4, 5]

        merged_linked_list: ListNode = self.sol.mergeTwoLists(
            self.load_linked_list(linked_list1),
            self.load_linked_list(linked_list2)
        )
        merged_list: List = self.load_list_from_linked_list(merged_linked_list);

        self.assertEqual([1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5], merged_list)

        linked_list1: List = []
        linked_list2: List = [0]

        merged_linked_list: ListNode = self.sol.mergeTwoLists(
            self.load_linked_list(linked_list1),
            self.load_linked_list(linked_list2)
        )
        merged_list: List = self.load_list_from_linked_list(merged_linked_list);

        self.assertEqual([0], merged_list)

    def test_two_way(self):
        linked_list: List[int] = [1, 2, 3, 4, 5]
        node: ListNode = self.load_linked_list(linked_list)

        converted_list = self.load_list_from_linked_list(node)

        self.assertEqual([1, 2, 3, 4, 5], converted_list)

    def test_deleteNode(self):
        linked_list: List[int] = [1, 2, 3, 4, 5]
        node: ListNode = self.load_linked_list(linked_list)

        self.sol.deleteNode(node.next.next)

        deleted_list = self.load_list_from_linked_list(node)

        self.assertEqual([1, 2, 4, 5], deleted_list)

    def test_remove_nth_from_end(self):
        linked_list: List[int] = [1, 2, 3, 4, 5]
        node: ListNode = self.load_linked_list(linked_list)
        node2: ListNode = self.load_linked_list(linked_list)

        node = self.sol.removeNthFromEnd(node, 2)
        node2 = self.sol.removeNthFromEnd(node2, 4)

        converted_list = self.load_list_from_linked_list(node)
        converted_list2 = self.load_list_from_linked_list(node2)

        self.assertEqual([1, 2, 3, 5], converted_list)
        self.assertEqual([1, 3, 4, 5], converted_list2)

    def test_remove_nth_from_beginning(self):
        linked_list: List[int] = [1, 2, 3, 4, 5]
        node: ListNode = self.load_linked_list(linked_list)
        node2: ListNode = self.load_linked_list(linked_list)

        node = self.sol.removeNthFromBeginning(node, 2)
        node2 = self.sol.removeNthFromBeginning(node2, 0)

        converted_list = self.load_list_from_linked_list(node)
        converted_list2 = self.load_list_from_linked_list(node2)

        self.assertEqual([1, 2, 4, 5], converted_list)
        self.assertEqual([2, 3, 4, 5], converted_list2)

    def test_reverse_linked_list(self):
        linked_list: List[int] = [1, 2, 3, 4, 5]
        node: ListNode = self.load_linked_list(linked_list)
        reversed_list: List = self.load_list_from_linked_list(self.sol.reverseList(node))
        self.assertEqual([5, 4, 3, 2, 1], reversed_list)

        linked_list: List[int] = [1]
        node: ListNode = self.load_linked_list(linked_list)
        reversed_list: List = self.load_list_from_linked_list(self.sol.reverseList(node))
        self.assertEqual([1], reversed_list)

        linked_list: List[int] = [1, 2]
        node: ListNode = self.load_linked_list(linked_list)
        reversed_list: List = self.load_list_from_linked_list(self.sol.reverseList(node))
        self.assertEqual([2, 1], reversed_list)

        linked_list: List[int] = [1, 2, 3]
        node: ListNode = self.load_linked_list(linked_list)
        reversed_list: List = self.load_list_from_linked_list(self.sol.reverseList(node))
        self.assertEqual([3, 2, 1], reversed_list)
