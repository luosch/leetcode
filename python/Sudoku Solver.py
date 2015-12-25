class Solution(object):
    def solveSudoku(self, board):
        def isValid(row, col):
            v = board[row][col];
            board[row][col] = 'K'

            for i in range(9):
                if board[i][col] == v:
                    return False
                if board[row][i] == v:
                    return False

            for i in range(3):
                for j in range(3):
                    if board[row // 3 * 3 + i][col // 3 * 3 + j] == v:
                        return False

            board[row][col] = v
            return True

        def dfs(row, col):
            if row >= 9:
                return True
            
            nextRow = row + 1 if col >= 8 else row
            nextCol = col + 1 if col <= 7 else 0
            
            if board[row][col] == '.':
                for k in '123456789':
                    board[row][col] = k
                    if isValid(row, col) and dfs(nextRow, nextCol):
                        return True
                board[row][col] = '.'
                return False
            else:
                return dfs(nextRow, nextCol)

        dfs(0, 0)
