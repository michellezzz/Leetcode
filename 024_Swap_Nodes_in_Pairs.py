# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


import tool

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if head is None:
            return head
        if head.next is None:
            return head
        else:
            new_head = head.next
            sub_list = self.swapPairs(new_head.next)
            new_head.next = head
            head.next = sub_list
            return new_head



a1 = tool.ListNode(1)
a2 = a1.next = tool.ListNode(2)
a3 = a2.next = tool.ListNode(3)
a4 = a3.next = tool.ListNode(4)
a5 = a4.next = tool.ListNode(5)
a6 = a5.next = tool.ListNode(6)
a7 = a6.next = tool.ListNode(7)
a8 = a7.next = tool.ListNode(8)

hi = Solution()

test_case = [
    #a1,
    #a7,
    a8,
    None
    ]# common

for item in test_case:
    print "\n\nInput:"
    tool.print_list(item)
    print "Output:"
    tool.print_list(hi.swapPairs(item))



