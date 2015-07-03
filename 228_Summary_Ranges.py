class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return []
        result = []
        start = nums[0]
        last = nums[0]
        del nums[0]
        nums.append(float("inf"))
        for i in nums:
            this = i
            if this != last + 1:
                if start == last:
                    result.append(str(last))
                else:
                    result.append(str(start) + '->' + str(last))
                start = this
            last = this
        return result

hi = Solution()
print hi.summaryRanges([0,1,2,4,5,7,9,10])
print hi.summaryRanges([])
print hi.summaryRanges([1])

