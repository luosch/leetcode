class Solution(object):
    def firstMissingPositive(self, nums):
        n, i = len(nums), 0
        while i < n:
            if nums[i] != i + 1 and 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                tmp = nums[i] - 1
                nums[i], nums[tmp] = nums[tmp], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
