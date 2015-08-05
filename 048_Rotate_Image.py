class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        size = len(matrix)
        up_left = 0
        down_right = size - 1
        for i in range(size/2):
            self.rotate_circle(matrix, up_left, down_right)
            up_left += 1
            down_right -= 1
        for line in matrix:
            print line

    def rotate_circle(self, matrix, up_left, down_right):
        for i in range(down_right - up_left):
            tmp1 = matrix[up_left][up_left + i]
            tmp2 = matrix[up_left + i][down_right]
            tmp3 = matrix[down_right][down_right - i]
            tmp4 = matrix[down_right - i][up_left]
            # print tmp1, tmp2, tmp3, tmp4

            matrix[up_left][up_left + i] = tmp4
            matrix[up_left + i][down_right] = tmp1
            matrix[down_right][down_right - i] = tmp2
            matrix[down_right - i][up_left] = tmp3

hi = Solution()

test_case = [
    [],

    [1],

    [
        [1,2],
        [3,4]
    ],

    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],

    [
        [ 1, 2, 3, 4, 5],
        [ 6, 7, 8, 9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]
    ]



    ]# common


for item in test_case:
    print "\n\nInput:"
    for line in item:
        print line
    print "Output:"
    hi.rotate(item)
