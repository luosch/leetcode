class Solution(object):
    used = None
    answer = 0
    size = 0
    
    def dfs(self, row, col):
        for i in range(0, self.size):
            if self.used[row][i] and i != col:
                return False
            if self.used[i][col] and i != row:
                return False
        
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if self.used[i][j]:
                return False
            i -= 1
            j -= 1

        i = row + 1
        j = col + 1
        while i < self.size and j < self.size:
            if self.used[i][j]:
                return False
            i += 1
            j += 1

        i = row - 1
        j = col + 1
        while i >= 0 and j < self.size:
            if self.used[i][j]:
                return False
            i -= 1
            j += 1

        i = row + 1
        j = col - 1
        while i < self.size and j >= 0:
            if self.used[i][j]:
                return False
            i += 1
            j -= 1

        if row == (self.size - 1):
            self.answer += 1

        for i in range(0, self.size):
            self.used[row + 1][i] = True
            self.dfs(row + 1, i)
            self.used[row + 1][i] = False
            
    def totalNQueens(self, n):
        self.used = [[False for col in range(n + 1)] for row in range(n + 1)]
        self.size = n
        self.answer = 0
        for i in range(0, n):
            self.used[0][i] = True
            self.dfs(0, i)
            self.used[0][i] = False
        
        return self.answer
