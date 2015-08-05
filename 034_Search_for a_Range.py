# I don't like this code
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        if target not in nums:
            return [-1, -1]
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1, -1]
        if nums[0] > target or nums[-1] < target:
            return [-1, -1]
        else:
            return [self.find_left(nums, target), self.find_right(nums, target)]#, self.find_right(nums, target)]

    def find_left(self, nums, target):
        if nums[0] == target:
            return 0

        bound_left = 0
        bound_right = len(nums) - 1
        while True:
            middle = (bound_left + bound_right)/2
            if nums[middle] == target:
                if nums[middle-1] < target:
                    return middle
                else:
                    bound_right = middle
                    continue
            elif nums[middle] < target:
                bound_left = middle + 1
                continue
            elif nums[middle] > target:
                bound_right = middle - 1
                continue

    def find_right(self, nums, target):
        if nums[-1] == target:
            return len(nums) - 1

        bound_left = 0
        bound_right = len(nums) - 1
        while True:
            middle = (bound_left + bound_right)/2
            if nums[middle] == target:
                if nums[middle+1] > target:
                    return middle
                else:
                    bound_left = middle + 1
                    continue
            elif nums[middle] < target:
                bound_left = middle + 1
                continue
            elif nums[middle] > target:
                bound_right = middle - 1
                continue


hi = Solution()

test_case = [
    ([1, 1, 1, 1, 1, 1], 1),
    ([1, 2, 2, 3], 2),
    ([1, 2, 2, 3], 6),
    ([3, 4, 5, 6], 1),
    ([1, 5], 4),
    ([3, 4, 5, 6], 6)

]

for item in test_case:
    print "Input:", item, " output:", hi.searchRange(item[0], item[1])