class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        result = []
        for i in range(len(nums)):
            new_nums = nums[:i] + nums[i+1:]
            a = self.permute(new_nums)
            for item in a:
                result.append([nums[i]] + item)
        return result

hi = Solution()

test_case = [
    [1, 2, 3, 4],
    [1, 2, 3],
    [1, 2],
    [1]
]  # common

for item in test_case:
    print "Input:", item, " output:", hi.permute(item)
