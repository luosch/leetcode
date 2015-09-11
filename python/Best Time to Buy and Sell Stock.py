class Solution(object):
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0

        answer = prices[1] - prices[0]
        if answer < 0: answer = 0
        dp = [0] * len(prices)
        
        for i in range(1, len(prices)):
            dp[i] = max(dp[i - 1] + prices[i] - prices[i - 1], prices[i] - prices[i - 1])
            answer = max(answer, dp[i])
        
        return answer
