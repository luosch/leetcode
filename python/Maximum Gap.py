class Solution(object):
    def maximumGap(self, nums):
        nums.sort()
        answer = 0
        for i in range(1, len(nums)):
            answer = max(answer, nums[i] - nums[i - 1])
        return answer
