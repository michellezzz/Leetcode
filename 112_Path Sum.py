# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if root:
            if root.left == None and root.right == None:
                return sum == root.val
            if self.hasPathSum(root.left, sum-root.val):
                return True
            if self.hasPathSum(root.right, sum-root.val):
                return True
        return False

a = TreeNode(5)
b0 = a.left = TreeNode(4)
b1 = a.right = TreeNode(8)
c0 = b0.left = TreeNode(11)
c1 = b1.left = TreeNode(13)
c2 = b1.right = TreeNode(4)

d0 = c0.left = TreeNode(7)
d1 = c0.right = TreeNode(2)
d2 = c2.right = TreeNode(1)

hi = Solution()
print hi.hasPathSum(a, 22)
