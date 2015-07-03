class Solution:
    '''
    @param integer[] nums
    @return integer
    '''
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        else:
            new_len = 1
            last = nums[0]

            i = 1
            while True:
                if i == len(nums):
                    break
                if nums[i] != last:
                    new_len += 1
                    last = nums[i]
                else:
                    del nums[i]
                    i -= 1
                i += 1

            return new_len


hi = Solution()

test_case = [
    [],
    [1],
    [1,2],
    [1,1],
    [1,1,2],
    [1,1,3,5,5],
    [1,1,1,1,1,1,1]

]  # common

for item in test_case:
    print "Input:", item, " output:", hi.removeDuplicates(item)