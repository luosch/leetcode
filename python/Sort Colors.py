class Solution(object):
    def sortColors_slow(self, nums):
        base = [0] * 3
        
        for num in nums:
            base[num] += 1
        
        for i in range(len(nums)):
            if 0 <= i < base[0]:
                nums[i] = 0
            elif base[0] <= i < base[0] + base[1]:
                nums[i] = 1
            else:
                nums[i] = 2

    def sortColors(self, nums):
        left = 0
        right = len(nums) - 1
        zero = 0
        
        while left <= right:
            if nums[left] == 0:
                nums[left], nums[zero] = nums[zero], nums[left]
                left += 1
                zero += 1
            elif nums[left] == 1:
                left += 1
            elif nums[left] == 2:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
