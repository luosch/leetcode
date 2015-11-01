class Solution(object):
    def rob_slow(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, n):
            dp.append(max(dp[i - 1], dp[i - 2] + nums[i]))
        return dp[-1]

    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        elif n < 3:
            return max(nums)
        
        first, second = 0, 0
        
        for i in xrange(n):
            first, second = second, max(first + nums[i], second)

        return second
