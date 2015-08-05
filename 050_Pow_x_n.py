class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1.0/self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        else:
            # return self.myPow(x, n/2) * self.myPow(x, n/2)
            # this line will cause time limit exceed
            return self.myPow(x, n/2)**2

hi = Solution()

test_case = [
    (0,0),
    (1,10),
    (10,1),
    (3, 4),
    (3, -4)
    ]# common


for item in test_case:
    print "\n\nInput:", item, "  output", hi.myPow(item[0], item[1])

