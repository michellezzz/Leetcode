class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        matrix = []
        for i in range(n):
            matrix.append([])
            for j in range(n):
                matrix[i].append(0)

        count = 1
        for i in range(0, n/2):
            count = self.fill_circle(matrix, i, n-1-i, count)
            print count
        if n % 2:
            matrix[n/2][n/2] = count
        return matrix

    def fill_circle(self, matrix, a, d, count):
        for i in range(a, d):
            matrix[a][i] = count
            count += 1
        for i in range(a, d):
            matrix[i][d] = count
            count += 1
        for i in range(d, a, -1):
            matrix[d][i] = count
            count += 1
        for i in range(d, a, -1):
            matrix[i][a] = count
            count += 1
        return count


hi = Solution()

test_case = [
    0, 1, 2, 3, 4
]

for item in test_case:
    print "Input:", item
    print " output:"
    for line in hi.generateMatrix(item):
        print line
