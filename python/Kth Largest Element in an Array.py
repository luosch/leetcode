class Solution(object):
    def findKthLargest(self, nums, k):
        pivot = nums[0]
        
        left = [num for num in nums if num < pivot]
        mid = [num for num in nums if num == pivot]
        right = [num for num in nums if num > pivot]
        
        if k <= len(right):
            return self.findKthLargest(right, k)
        elif k - len(right) <= len(mid):
            return mid[0]
        else:
            return self.findKthLargest(left, k - len(right) - len(mid))
