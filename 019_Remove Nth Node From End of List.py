import tool

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        if n == 0:
            return head
        p1 = head
        p2 = head
        for i in range(n):
            p1 = p1.next
            if p1 is None:
                return head.next
        while p1.next is not None:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return head


a1 = tool.ListNode(1)
a2 = a1.next = tool.ListNode(2)
a3 = a2.next = tool.ListNode(3)
'''
a4 = a3.next = tool.ListNode(4)
a5 = a4.next = tool.ListNode(5)
a6 = a5.next = tool.ListNode(6)
a7 = a6.next = tool.ListNode(7)
a8 = a7.next = tool.ListNode(8)
'''

hi = Solution()

test_case = [
    #(a1, 0),
    #(a1, 1),
    #(a1, 2),
    (a1, 3)
    #(a3, 2)
    ]# common


for item in test_case:
    print "\n\nInput:"
    tool.print_list(item[0])
    print item[1]
    print "Output:"
    tool.print_list(hi.removeNthFromEnd(item[0], item[1]))

