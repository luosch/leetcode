class Solution(object):
    def minSubArrayLen(self, s, nums):
        left, right, tmp, n = 0, 0, 0, len(nums)
        answer = n
        while right < n:
            tmp += nums[right]
            right += 1
            if tmp >= s:
                while tmp - nums[left] >= s:
                    tmp -= nums[left]
                    left += 1
                answer = min(answer, right - left)
        
        if tmp < s:
            answer = 0
        
        return answer
