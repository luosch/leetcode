class Solution(object):
    def candy(self, ratings):
        n = len(ratings)
        nums = [1 for _ in range(n)]
        
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                nums[i] = nums[i - 1] + 1
        
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and nums[i] <= nums[i + 1]:
                nums[i] = nums[i + 1] + 1
        
        
        return reduce(lambda x, y: x + y, nums)
