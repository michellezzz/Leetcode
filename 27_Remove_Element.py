class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        i = 0
        new_length = 0
        while True:
            if i == len(nums):
                break
            if nums[i] == val:
                del nums[i]
                i -= 1
            else:
                new_length += 1
            i += 1
        return new_length

hi = Solution()

test_case = [
    ([],0),
    ([1],1),
    ([1,2],1),
    ([1,1],1),
    ([1,1,2],1),
    ([1,1,3,5,5],1),
    ([1,1,1,1,1,1,1],1)

]  # common

for item in test_case:
    print "Input:", item, " output:", hi.removeElement(item[0], item[1])
