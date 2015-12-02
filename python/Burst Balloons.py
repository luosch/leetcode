class Solution(object):
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in xrange(n)]
        for l in xrange(2, n):
            for left in xrange(0, n - l):
                right = left + l
                for k in xrange(left + 1, right):
                    dp[left][right] = max(dp[left][right],                         nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right])
        
        return dp[0][n - 1]
