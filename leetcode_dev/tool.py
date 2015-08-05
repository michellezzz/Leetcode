__author__ = 'michelle'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_list(head):
    if not head:
        print "Empty",
    else:
        p = head
        while p:
            print p.val,
            p = p.next
    print " | ",


'''  define a list
a1 = tool.ListNode(1)
a2 = a1.next = tool.ListNode(2)
a3 = a2.next = tool.ListNode(3)
a4 = a3.next = tool.ListNode(4)
a5 = a4.next = tool.ListNode(5)
a6 = a5.next = tool.ListNode(6)
a7 = a6.next = tool.ListNode(7)
a8 = a7.next = tool.ListNode(8)

'''

