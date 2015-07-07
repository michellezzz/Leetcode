class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        k = (m+n)/2
        #print "k is %d" % k

        if len(nums1) == 0 and len(nums2) == 0:
            return 0

        if (m+n)%2 != 0:
            return self.find_k_th_smallest(k+1, nums1, nums2)
        else:
            return (self.find_k_th_smallest(k, nums1, nums2) + self.find_k_th_smallest(k+1, nums1, nums2))/2.0


    def find_k_th_smallest(self, k, nums1, nums2):
        #print "this is find %dth smallest in list %s and %s"% (k, str(nums1), str(nums2))
        if len(nums1) == 0 and len(nums2) == 0:
            return 0
        if len(nums1) == 0:
            return nums2[k-1]
        if len(nums2) == 0:
            return nums1[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])

        p1 = p2 = k/2-1
        if len(nums1) < k/2:
            p1 = len(nums1) -1
        if len(nums2) < k/2:
            p2 = len(nums2) -1


        if nums1[p1] <= nums2[p2]:
            #print "state1"
            return self.find_k_th_smallest(k-p1-1, nums1[p1+1:], nums2)
        if nums1[p1] > nums2[p2]:
            #print "state2"
            return self.find_k_th_smallest(k-p2-1, nums1, nums2[p2+1:])


hi = Solution()

test_case = [
    ([], []),
    ([1], [0]),
    ([1], [1]),
    ([1, 2, 3], [4]),
    ([2], []),
    ([1], [2,3,4,5,6]),
    ([], [1,2,3,4,5])
]  # common

for item in test_case:
    print "Input:", item, " output:", hi.findMedianSortedArrays(item[0], item[1])