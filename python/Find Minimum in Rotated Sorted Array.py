class Solution(object):
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        mid = (left + right) / 2
        while left <= right:
            if nums[left] <= nums[right]:
                return nums[left]
            mid = (left + right) / 2
            if (nums[mid] >= nums[left]):
                left = mid + 1
            else:
                right = mid
        
        return nums[mid]
