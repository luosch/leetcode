class Solution(object):
    def maxProfit(self, prices):
        profits = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        return sum(filter(lambda x: x > 0, profits))
        
