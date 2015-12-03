class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if len(nums) <= 1:
            return nums

        from collections import deque
        answer = []
        q = deque([])
        
        for i in range(len(nums)):
            if q and q[0] == i - k:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                answer.append(nums[q[0]])
        
        return answer
