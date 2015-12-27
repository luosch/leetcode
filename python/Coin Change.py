class Solution(object):
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in xrange(1, amount + 1):
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return -1 if dp[amount] > amount else dp[amount]
