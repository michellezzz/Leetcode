import math
new_sysmax = int(math.pow(2,31)-1)

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        if(x > new_sysmax or x < -1*new_sysmax):
            return 0
        if x == 0:
            return 0
        elif x > 0:
            flag = 1
        elif x < 0:
            flag = -1
            x = -x
        result = 0
        while x != 0:
            tmp = x % 10
            x /= 10
            result = result*10 + tmp
        if(result > new_sysmax or result < -1*new_sysmax):
            return 0
        return flag * result

hi = Solution()
print hi.reverse(1534236469)
