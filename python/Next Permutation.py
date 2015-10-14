class Solution(object):
    def nextPermutation(self, nums):
        cursor = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                cursor = i - 1
                break
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[cursor]:
                nums[i], nums[cursor] = nums[cursor], nums[i]
                nums[cursor + 1:] = sorted(nums[cursor + 1:])
                break
