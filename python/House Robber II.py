class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        elif n < 4:
            return max(nums)
        
        first, second = 0, 0
        
        for i in xrange(0, n - 1):
            first, second = second, max(first + nums[i], second)

        tmp = second
        first, second = 0, 0
        
        for i in xrange(1, n):
            first, second = second, max(first + nums[i], second)

        return max(tmp, second)
