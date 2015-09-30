class Solution(object):
    def moveZeroes(self, nums):
        zeroCount = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1
            else:
                nums[i - zeroCount] = nums[i]
        for i in range(1, zeroCount + 1):
            nums[-i] = 0
