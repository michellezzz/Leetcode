class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        if nums == []:
            return 0
        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        middle = len(nums)/2

        if target == nums[middle]:
            return middle
        else:
            if target < nums[middle]:
                return self.searchInsert(nums[0:middle], target)
            else:
                return middle + 1 + self.searchInsert(nums[middle+1:], target)


hi = Solution()

test_case = [
    ([],1),
    ([1,3,5],1),
    ([1,3,5],2),
    ([1,3,5],3),
    ([1,3,5],4),
    ([1,3,5],5),
    ([1,3,5],6)
]  # common

for item in test_case:
    print "Input:", item, " output:\n", hi.searchInsert(item[0],item[1])
