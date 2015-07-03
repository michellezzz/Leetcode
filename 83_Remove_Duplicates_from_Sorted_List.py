# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        this = head
        while this:
            if this.next == None:
                return head
            elif this.next.val == this.val:
                this.next = this.next.next
            else:
                this = this.next
        return head

a0 = ListNode(1)
a1 = a0.next = ListNode(1)
a2 = a1.next = ListNode(1)
a3 = a2.next = ListNode(1)
a4 = a3.next = ListNode(1)
a5 = a4.next = ListNode(1)

hi = Solution()
hi.deleteDuplicates(a0)

this = a0
while this:
    print this.val
    this = this.next
