class Solution(object):
    def exist(self, board, word):
        m, n = len(board), len(board[0])
        def dfs(x, y, word):
            if len(word) == 0:
                return True
            # up
            if x > 0 and board[x - 1][y] == word[0]:
                tmp = board[x][y]
                board[x][y] = '#'
                if dfs(x - 1, y, word[1:]):
                    return True
                board[x][y] = tmp
            # down
            if x < m - 1 and board[x + 1][y] == word[0]:
                tmp = board[x][y]
                board[x][y] = '#'
                if dfs(x + 1, y, word[1:]):
                    return True
                board[x][y] = tmp
            # left
            if y > 0 and board[x][y - 1] == word[0]:
                tmp = board[x][y]
                board[x][y] = '#'
                if dfs(x, y - 1, word[1:]):
                    return True
                board[x][y] = tmp
            # right
            if y < n - 1 and board[x][y + 1] == word[0]:
                tmp = board[x][y]
                board[x][y] = '#'
                if dfs(x, y + 1, word[1:]):
                    return True
                board[x][y] = tmp
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, word[1:]):
                        return True
        return False
