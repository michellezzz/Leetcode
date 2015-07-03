#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    # Given two binary trees, write a function to check if they are equal or not.
    # Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
    def isSameTree(self, p, q):
        if not (p and q):
            if p or q:
                return False
            else:
                return True
        if p.val != q.val:
            return False
        else:
            if not (p.left or p.right or q.left or q.right):
                return True
            else:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


p = TreeNode(3)
p.left = TreeNode(1)
p.right = TreeNode(2)

q = TreeNode(2)


hi = Solution()

test_case = [
    [None, None],
    [p, None],
    [p, q],
    [p, p],
    [q,q]
]  # common

for item in test_case:
    print "Input:", item, " output:", hi.isSameTree(item[0], item[1])