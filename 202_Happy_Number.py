class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        sum = n
        sum_list = []
        while sum != 1:
            tmp = sum
            sum = 0
            while tmp!=0:
                sum += (tmp%10)**2
                tmp = tmp/10
            if sum in sum_list:
                return False
            else:
                sum_list.append(sum)
        return True

hi = Solution()
for i in range (0, 20):
    print i, hi.isHappy(i)
