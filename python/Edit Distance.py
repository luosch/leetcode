class Solution(object):
    def minDistance(self, word1, word2):
        m, n = len(word1) + 1, len(word2) + 1
        
        if m == 1 or n == 1:
            return max(m, n) - 1
        
        dp = [[0 for _ in range(n)] for __ in range(m)]
        
        for i in range(m):
            dp[i][0] = i
        
        for i in range(n):
            dp[0][i] = i
        
        for i in range(1, m):
            for j in range(1, n):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
        
        return dp[-1][-1]
