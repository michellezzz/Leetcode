class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def translate(self, num):
        if num == 1:
            return 0
        if num == -1:
            return 1
        else:
            return num

    def uniquePathsWithObstacles(self, obstacleGrid):
        if len(obstacleGrid) == 0:
            return 0
        if len(obstacleGrid[0]) == 0:
            return 0

        for i in range(len(obstacleGrid)-1, -1, -1):
            for j in range(len(obstacleGrid[0])-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    continue
                if i == len(obstacleGrid) - 1:
                    if j == len(obstacleGrid[0])-1:
                        if obstacleGrid[i][j] == 1:
                            return 0
                        else:
                            obstacleGrid[i][j] = -1
                    else:
                        if obstacleGrid[i][j+1] == 1:
                            obstacleGrid[i][j] = 0
                        elif obstacleGrid[i][j+1] == -1:
                            obstacleGrid[i][j] = -1
                        elif obstacleGrid[i][j+1] == 0:
                            obstacleGrid[i][j] = 0
                elif j == len(obstacleGrid[0]) - 1:
                    if obstacleGrid[i+1][j] == 1:
                        obstacleGrid[i][j] = 0
                    elif obstacleGrid[i+1][j] == -1:
                        obstacleGrid[i][j] = -1
                    elif obstacleGrid[i+1][j] == 0:
                        obstacleGrid[i][j] = 0
                else:
                    tmp1 = self.translate(obstacleGrid[i+1][j])
                    tmp2 = self.translate(obstacleGrid[i][j+1])
                    if tmp1 + tmp2 == 1:
                        obstacleGrid[i][j] = -1
                    else:
                        obstacleGrid[i][j] = tmp1 + tmp2




        #for item in obstacleGrid:
        #    print item


        return self.translate(obstacleGrid[0][0])





hi = Solution()

test_case = [
    [],

    [
        [0]
    ],

    [
        [1]
    ],

    [
        [0,1]
    ],

    [
        [1],
        [0]
    ],

    [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ],

    [
        [0,0,0],
        [0,0,1],
        [0,1,0]
    ],

    [
        [0,0,0],
        [0,0,1],
        [0,0,0]
    ],

    [
        [0,0,0],
        [0,0,0],
        [0,0,1]
    ],

    [
        [1,0,0],
        [0,0,0],
        [0,0,0]
    ]


]  # common

for item in test_case:
    print "Input:", item, " output:\n", hi.uniquePathsWithObstacles(item)
