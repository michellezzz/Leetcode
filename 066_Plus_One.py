class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        length = len(digits)
        for i in range(length-1, -1, -1):
            if digits[i]!=9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        if i == 0:
            return [1] + digits
            

hi = Solution()
print hi.plusOne([9,9,9,9,9,9])


