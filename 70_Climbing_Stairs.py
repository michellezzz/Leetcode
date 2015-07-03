class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n==1 or n == 2:
            return n
        a = 1
        b = 2
        for i in range (0,n-2):
            b,a = a+b,b
        return b
            


hi = Solution()
for i in range (1,10):
    print hi.climbStairs(i)

