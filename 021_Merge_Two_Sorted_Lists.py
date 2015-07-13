# Definition for singly-linked list.
import tool

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        p1 = l1
        p2 = l2
        head = ListNode(-999)
        p = head

        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        if p1:
            p.next = p1
        elif p2:
            p.next = p2

        return head.next


a0 = ListNode(1)
a1 = a0.next = ListNode(3)
a2 = a1.next = ListNode(5)

b0 = ListNode(2)
b1 = b0.next = ListNode(4)
b2 = b1.next = ListNode(6)

hi = Solution()

test_case = [
    (None, None),
    (a0, None),
    (a0, b0)
]  # common

for item in test_case:
    print "\n\nInput:", item, " \noutput:"
    tool.print_list(hi.mergeTwoLists(item[0], item[1]))