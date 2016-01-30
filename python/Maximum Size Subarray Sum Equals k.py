class Solution(object):
    def maxSubArrayLen(self, nums, k):
        sum_index = {0: -1}
        answer = tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            if tmp not in sum_index:
                sum_index[tmp] = i
            if tmp - k in sum_index:
                answer = max(answer, i - sum_index[tmp - k])
        
        return answer
