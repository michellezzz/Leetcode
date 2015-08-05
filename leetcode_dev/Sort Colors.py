class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        if len(nums) <= 1:
            return nums
        left = 0  # first item from the left which is not 0
        middle = 0  # first item from the left which is 2
        right = len(nums) - 1  # first item from the right which is not 2
        while True:
            while nums[left] == 0:
                left += 1
            while nums[right] == 2:
                right -= 1
            while nums[middle] != 2:
                if nums[middle] == 0:
                    nums[left], nums[middle] = nums[middle], nums[left]
                    left+=1
                    middle+=1
                    print "swap:", left, middle
                middle += 1
            if middle >= right or left>= middle:
                break
            nums[middle], nums[right] = nums[right], nums[middle]
            print "swap:", middle, right
            continue


        print nums



hi = Solution()

test_case = [
    [0,1,2,0,1,2],
    [1,2,2,0,0,2,1],
    [2,0]
    ]# common

for item in test_case:
    print "Input:", item, " output:\n", hi.sortColors(item)



