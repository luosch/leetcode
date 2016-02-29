class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = [0, k, k*k, 0]
        if n <= 2:
            return dp[n]
        
        for i in range(3, n + 1):
            dp[3] = (k-1) * dp[1] + (k-1) * dp[2]
            dp[1] = dp[2]
            dp[2] = dp[3]
        
        return dp[3]
