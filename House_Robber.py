
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            result = {}
            result[0] = 0
            result[1] = nums[0]
            for i in range (2, len(nums)+1):
                result[i] = max(result[i-1], result[i-2] + nums[i-1])
            return result[len(nums)]
                
        
hi = Solution()
print hi.rob([])
print hi.rob([1])
print hi.rob([1,2])
print hi.rob([1,2,3])
print hi.rob([4,2,5,43,20,50,100,3])
