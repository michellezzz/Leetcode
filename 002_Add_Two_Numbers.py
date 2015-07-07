"""
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

def print_list(head):
    if not head:
        print "Empty",
    else:
        p = head
        while p:
            print p.val,
            p = p.next
    print " | ",


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        if not(l1 or l2):
            return None

        carry = 0
        p1 = l1
        p2 = l2
        p_res = ListNode(9999)
        result = p_res

        while p1 or p2 or carry!=0:
            if p1:
                a1 = p1.val
            else:
                a1 = 0
            if p2:
                a2 = p2.val
            else:
                a2 = 0

            p_res.next = ListNode((a1 + a2 + carry) % 10)
            carry = (a1 + a2 + carry) / 10

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
            p_res = p_res.next

        return result.next


a1 = ListNode(9)
a2 = a1.next = ListNode(9)
a3 = a2.next = ListNode(9)

b1 = ListNode(2)
b2 = b1.next = ListNode(3)


hi = Solution()

test_case = [
    (None, None),
    (a1, None),
    (a1, b1),
    (a3, b2)
]  # common


for item in test_case:
    print "\n\nInput:",
    print_list(item[0])
    print_list(item[1])
    print "\nOutput: ",
    print_list(hi.addTwoNumbers(item[0], item[1]))
