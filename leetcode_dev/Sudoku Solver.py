class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        board_list = []
        ready_queue = []

        for i in range(0, 9):
            bad_set = board[i]   # for each row, find a bad set
            board_list.append([])
            for j in range(0, 9):
                if board[i][j] == '.':
                    board_list[i].append([])
                    for num in range(1, 9):
                        if str(num) not in bad_set:
                            board_list[i][j].append(num)
                else:
                    board_list[i].append(board[i][j])

        for j in range(0, 9):
            bad_set = ''
            for i in range(0, 9):
                bad_set += board[i][j]  # for each column, find a bad set
            for i in range(0, 9):
                if type(board_list[i][j]) is list:
                    temp = []
                    for item in board_list[i][j]:
                        if str(item) not in bad_set:
                            temp.append(item)
                    board_list[i][j] = temp

        index = [[0, 1, 2], [3, 4, 5], [6, 8, 7]]
        for index1 in range(0, 3):
            for index2 in range(0, 3):
                bad_set = ''
                for i in index[index1]:
                    for j in index[index2]:
                        bad_set += board[i][j]  #  for each block, find a bad set
                for i in index[index1]:
                    for j in index[index2]:
                        if type(board_list[i][j]) is list:
                            temp = []
                            for item in board_list[i][j]:
                                if str(item) not in bad_set:
                                    temp.append(item)
                            board_list[i][j] = temp
                            if len(temp) == 1:
                                # print temp, i ,j
                                ready_queue.append((i, j))

        while ready_queue:
            r1, r2 = ready_queue.pop()   # board_list[r1][r2] contains only one choice

            if type(board_list[r1][r2]) is list:
                if len(board_list[r1][r2]) == 0:
                    break
                number = board_list[r1][r2][0]
                print r1, r2, number
                board_list[r1][r2] = str(number)

                i = r1
                for j in range(0, 9):
                    if type(board_list[i][j]) is list:
                        if number in board_list[i][j]:
                            board_list[i][j].remove(number)
                        if len(board_list[i][j]) == 1:
                            ready_queue.append((i,j))

                j = r2
                for i in range(0, 9):
                    if type(board_list[i][j]) is list:
                        if number in board_list[i][j]:
                            board_list[i][j].remove(number)
                        if len(board_list[i][j]) == 1:
                            ready_queue.append((i, j))

                for i in range(r1/3, r1/3 + 3):
                    for j in range(r2/3, r2/3 + 3):
                        if type(board_list[i][j]) is list:
                            if number in board_list[i][j]:
                                board_list[i][j].remove(number)
                            if len(board_list[i][j]) == 1:
                                ready_queue.append((i, j))

        for item in board_list:
            print item

hi = Solution()

test_case = [
    ['53..7....',
     '6..195...',
     '.98....6.',
     '8...6...3',
     '4..8.3..1',
     '7...2...6',
     '.6....28.',
     '...419..5',
     '....8..79'
     ]
]  # common

for item in test_case:
    print "Input:", item, " output:\n", hi.solveSudoku(item)




