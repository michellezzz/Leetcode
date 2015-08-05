class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        m = len(matrix)
        n = len(matrix[0])
        result = []

        i = 0
        while True:
            result.extend(self.circle_order(matrix, i, i, m-1-i, n-1-i))
            if i == m-1-i or i == m-2-i or i == n-1-i or i == n-2-i:
                break
            else:
                i += 1

        return result

    def circle_order(self, matrix, a, b, c, d):
        print "circle:", a, b, c, d
        if a == c:
            return matrix[a][b:d+1]
        result = []
        if b == d:
            for i in range(a, c+1):
                result.append(matrix[i][b])
            return result
        for i in range(b, d):
            result.append(matrix[a][i])
        for i in range(a, c):
            result.append(matrix[i][d])
        for i in range(d, b, -1):
            result.append(matrix[c][i])
        for i in range(c, a, -1):
            result.append(matrix[i][b])
        return result

hi = Solution()

test_case = [
    [],

    [
        [1]
    ],

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
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ],

    [
        [ 1, 2, 3, 4, 5],
        [ 6, 7, 8, 9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]
    ],

    [
        [1,2,3]
    ],

    [
        [1],
        [2],
        [3]
    ],

    [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [10,11,12]
    ],

    [
        [1,2,3,4,5,6,7,8,9,10],
        [11,12,13,14,15,16,17,18,19,20]
    ]

    ]# common


for item in test_case:
    print "\n\nInput:"
    for line in item:
        print line
    print "Output:"
    print(hi.spiralOrder(item))

