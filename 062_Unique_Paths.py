class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        m-=1
        n-=1
        last_array = []
        for i in range(m+1):
            last_array.append(1)
        this_array = last_array

        for i in range(n):
            for j in range(1, m+1):
                this_array[j] = this_array[j-1] + last_array[j]
            last_array = this_array
        return this_array[-1]


hi = Solution()

test_case = [
    (1,1),
    (1,5),
    (2,5),
    (4,6)
]  # common

for item in test_case:
    print "Input:", item, " output:", hi.uniquePaths(item[0], item[1])
