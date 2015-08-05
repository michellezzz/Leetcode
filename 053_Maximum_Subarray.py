class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        the_max = nums[0]
        tem_max = nums[0]
        for i in range(1, len(nums)):
            if tem_max <= 0:
                tem_max = max(tem_max, nums[i])
            else:
                tem_max += nums[i]
            if tem_max > the_max:
                the_max = tem_max
        return the_max

hi = Solution()

test_case = [
    [-2],
    [1, -2],
    [1, -1],
    [-2, 1],
    [-3, -2],
    [-10, -2, -3, -4],
    [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ]# common

for item in test_case:
    print "Input:", item, " output:", hi.maxSubArray(item)


