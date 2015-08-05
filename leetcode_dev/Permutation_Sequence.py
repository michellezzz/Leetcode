import math

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        result = ''
        p = n-1
        result += str((k-1)/math.factorial(p) + 1)
        return result



hi = Solution()

test_case = [
    (3,1),
    (3,2),
    (3,3),
    (3,4),
    (3,5),
    (3,6)
    ]# common

for item in test_case:
    print "Input:", item, " output:", hi.getPermutation(item[0], item[1])