class Solution(object):
    def findPeakElement(self, nums):
        if not nums:
            return None
        left, right = 0, len(nums) - 1
        while left <= right:
            if left == right:
                return left
            mid = (left + right) / 2
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        
        return mid
