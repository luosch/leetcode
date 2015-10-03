class Solution(object):
    def findDuplicate_binary(self, nums):
        left, right, count = 1, len(nums) - 1, 0
        while left < right:
            mid = (left + right) / 2
            count = 0
            for item in nums:
                if item <= mid:
                    count += 1
            
            if count > mid:
                right = mid
            else:
                left = mid + 1
        
        return (left + right) / 2
        
    def findDuplicate(self, nums):
        if len(nums) > 1:
            slow, fast = nums[0], nums[nums[0]]
            while slow != fast:
                slow = nums[slow]
                fast = nums[nums[fast]]
            
            fast = 0
            
            while slow != fast:
                slow = nums[slow]
                fast = nums[fast]
            
            return slow
