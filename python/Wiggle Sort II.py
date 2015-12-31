class Solution(object):
    def wiggleSort(self, nums):
        nums.sort()
        half = (len(nums) + 1) // 2
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
