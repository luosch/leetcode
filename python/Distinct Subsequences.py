class Solution(object):
    def numDistinct(self, s, t):
        t_len = len(t)
        dp = [0] * (t_len + 1)
        dp[0] = 1
        
        for c in s:
            for i in range(t_len - 1, -1, -1):
                if t[i] == c:
                    dp[i + 1] += dp[i]
        
        return dp[-1]
