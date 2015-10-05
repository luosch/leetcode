class Solution(object):
    def gameOfLife(self, board):
        if len(board) < 1:
            return 
        col = len(board)
        row = len(board[0])
        for i in range(0, col):
            for j in range(0, row):
                if board[i][j] & 0x01 == 0:
                    continue
                if j + 1 < row:
                    board[i][j+1] += 2
                if j - 1 >= 0:
                    board[i][j-1] += 2
                if i + 1 < col:
                    board[i+1][j] += 2
                    if j + 1 < row:
                        board[i+1][j+1] += 2
                    if j - 1 >= 0:
                        board[i+1][j-1] += 2
                if i - 1 >= 0:
                    board[i-1][j] += 2
                    if j + 1 < row:
                        board[i-1][j+1] += 2
                    if j - 1 >= 0:
                        board[i-1][j-1] += 2
        for i in xrange(0, col):
            for j in xrange(0, row):
                if 4 < board[i][j] < 8:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
        return
