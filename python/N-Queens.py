class Solution(object):
    def solveNQueens(self, n):
        def helper(row):
            if row == n:
                matrix = []
                for i in range(n):
                    matrix.append('.' * state[i] + 'Q' + '.' * (n - state[i] - 1))
                answer.append(matrix)
                return

            for col in range(n):
                if isValid(row, col):
                    state[row] = col
                    helper(row + 1)
                    state[row] = -1
        
        def isValid(row, col):
            for i in range(row):
                if state[i] == col or abs(row - i) == abs(col - state[i]):
                    return False
            return True
        
        answer = []
        state = [-1] * n
        helper(0)
        
        return answer
