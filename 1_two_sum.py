"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2.
Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

class Solution:
# @param {integer[]} nums
# @param {integer} target
# @return {integer[]}
    def twoSum(self, nums, target):
        d = dict()
        for i, val in enumerate(nums):
            if target-val in d:
                return d[target-val], i+1
            else:
                d[val] = i+1

hi = Solution()

test_case = [
    ([-1, -2, -3, -4, -5], -8),
    ([0, 4, 3, 0], 0),
    ([], 0),
    ([],None),
    ([0, 0], 0),
    ([0], 0),

]  # common

for item in test_case:
    print "Input:", item, " output:", hi.twoSum(item[0], item[1])