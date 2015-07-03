class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):

        for i in range(0,9):
            for j in range(0, 9):
                if board[i][j] != '.':
                    if int(board[i][j]) > 9:
                        print "error0"
                        return False
                
        for i in range (0,9):
            tem_set = []
            for item in board[i]:
                if item != '.':
                    tem_set.append(item)
            if len(set(tem_set))<len(tem_set):
                print "error1"
                return False
            
        for i in range (0,9):
            tem_set = []
            for j in range(0,9):
                if board[j][i] != '.':
                    tem_set.append(board[j][i])
            if len(set(tem_set))<len(tem_set):
                print "error2"
                return False
            
        a = [[0,1,2], [3,4,5], [6,7,8]]

        for nums1 in a:
            for nums2 in a:
                tem_set = []
                for i in nums1:
                    for j in nums2:
                        if board[i][j] != '.':
                            tem_set.append(board[i][j])
                        if len(set(tem_set))<len(tem_set):
                            print "error3"
                            return False
        return True

d = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]

hi = Solution()
print hi.isValidSudoku(d)

