class Solution(object):
    def maximalSquare(self, matrix):
        if len(matrix) == 0:
            return 0
        
        m, n, answer = len(matrix), len(matrix[0]), 0
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0 and matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = int(matrix[i][j])
                answer = max(answer, dp[i][j])
        
        return answer ** 2
