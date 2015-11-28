class Solution(object):
    def maxProfit(self, prices):
        dp = [[float('-inf'), 0, float('-inf'), 0],             [float('-inf'), 0, float('-inf'), 0]]
        cur, next = 0, 1
        for price in prices:
            dp[next][0] = max(dp[cur][0], -price)
            dp[next][1] = max(dp[cur][1], dp[cur][0] + price)
            dp[next][2] = max(dp[cur][2], dp[cur][1] - price)
            dp[next][3] = max(dp[cur][3], dp[cur][2] + price)
            cur, next = next, cur
        return max(dp[cur][1], dp[cur][3])
