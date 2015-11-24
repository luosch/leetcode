class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        if n <= 1:
            return 0
        elif n == 2:
            return max(0, prices[1] - prices[0])
        
        dp = [[0]*n, [0]*n]
        dp[0][0] = -prices[0]
        dp[0][1] = max(-prices[0], -prices[1])
        dp[1][0] = 0
        dp[1][1] = max(0, prices[1] - prices[0])
        
        for i in range(2, n):
            dp[0][i] = max(dp[0][i - 1], dp[1][i - 2] - prices[i])
            dp[1][i] = max(dp[1][i - 1], dp[0][i - 1] + prices[i])
        
        return dp[1][n - 1]
