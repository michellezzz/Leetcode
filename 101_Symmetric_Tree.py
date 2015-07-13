# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tool import *

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if root is None:
            return True
        else:
            return self.isMirrorTree(root.left, root.right)

    def isMirrorTree(self, root1, root2):
        if not (root1 and root2):
            if root1 is None and root2 is None:
                return True
            else:
                return False

        if root1.val != root2.val:
            return False
        else:
            return self.isMirrorTree(root1.left, root2.right) and self.isMirrorTree(root1.right, root2.left)


p = TreeNode(3)
p.left = TreeNode(1)
p.right = TreeNode(2)

q = TreeNode(2)

hi = Solution()

test_case = [
    p, None, q
]  # common

for item in test_case:
    print "Input:", item, " output:", hi.isSymmetric(item)