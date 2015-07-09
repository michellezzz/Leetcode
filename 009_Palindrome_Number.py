import math

class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x == 0:
            return True

        length = math.floor(math.log10(x))
        dividend = 10**int(length)

        while x > 0:
            if x%10 != x/dividend:
                return False
            else:
                x = (x%dividend)/10
                dividend/=100
        return True

hi = Solution()

test_case = [
    -1,0,1,10,11,100,101,999,1000,1001,5005,11100011

]  # common

for item in test_case:
    print "Input:", item, " output:", hi.isPalindrome(item)