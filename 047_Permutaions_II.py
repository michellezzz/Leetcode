class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        result = []

        tmp = []
        for i in range(len(nums)):
            if nums[i] in tmp:
                continue
            tmp.append(nums[i])

            new_nums = nums[:i] + nums[i+1:]
            a = self.permuteUnique(new_nums)
            for item in a:
                result.append([nums[i]] + item)
        return result


hi = Solution()

test_case = [
    [1, 2, 3, 4],
    [1, 2, 3],
    [1, 2],
    [1],
    [1, 1],
    [1,1,2],
    [1,1,2,2]
]  # common

for item in test_case:
    print "Input:", item, " output:", hi.permuteUnique(item)