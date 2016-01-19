class Solution(object):
    def minCut(self, s):
        ls = len(s)
        dp = [0 for i in range(ls + 1)]
        p = [[False] * ls for j in range(ls)]
        for i in range(ls + 1):
            dp[i] = ls - i

        for i in range(ls - 1, -1, -1):
            for j in range(i, ls):
                if s[i] == s[j] and (((j - i) < 2) or p[i + 1][j - 1]):
                    p[i][j] = True
                    dp[i] = min(1 + dp[j + 1], dp[i])
                    
        return dp[0] - 1
