class Solution(object):
    def maxSubArray(self, nums):
        answer = nums[0]
        dp = [0] * len(nums)
        dp[0] = answer
        
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            answer = max(answer, dp[i])
            
        return answer
