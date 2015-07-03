"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2.
Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""
# TODO: bug  Input: ([0, 4, 3, 0], 0)  output: (0, 1)

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        new_nums = sorted(nums)
        index1 = None
        index2 = None

        i = 0
        for i in range(0, len(new_nums)):
            if new_nums[i] > target:
                break
        del new_nums[i+1:]

        for item in new_nums:
            if 2*item == target:
                if new_nums.count(item) > 1:
                    index1 = nums.index(item) + 1
                    del nums[index1]
                    index2 = nums.index(item)
            elif target-item in new_nums:
                index1 = nums.index(item) + 1
                index2 = nums.index(target - item) + 1
        return min(index1, index2), max(index1, index2)



hi = Solution()

test_case = [

    ([2, 14, 8, 11], 10),
    ([1], 10),
    ([1, 2], 10),
    ([5, 3, 7], 10),
    ([0, 4, 3, 0], 0),
    ([4, 4, 10], 8)
]  # common

for item in test_case:
    print "Input:", item, " output:", hi.twoSum(item[0], item[1])
