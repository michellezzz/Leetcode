import copy

class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        temp = copy.deepcopy(nums1[0:m])
        i = j = 0
        p = 0
        while i < m and j < n:
            if temp[i] <= nums2[j]:
                nums1[p] = temp[i]
                i += 1
            else:
                nums1[p] = nums2[j]
                j += 1
            p += 1
        if i == m:
            nums1[p:] = nums2[j:]
        else:
            nums1[p:] = temp[i:]
        # return nums1

hi = Solution()

test_case = [
    ([], 0, [], 0),
    ([1,2,3,0],3,[3],1),
    ([1],1,[],0),
    ([0,0,0],0,[1,2,3],3),
    ([1,3,5,0,0,0],3, [2,4,6],3)
]  # common

for item in test_case:
    print "\n\nInput:", item, " \noutput:", hi.merge(item[0], item[1],item[2],item[3])

