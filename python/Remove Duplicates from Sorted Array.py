class Solution(object):
    def removeDuplicates_slow(self, nums):
        cursor = 1
        count = 0
        while cursor < len(nums):
            if nums[cursor] == nums[cursor - 1]:
                del nums[cursor]
            else:
                cursor += 1
        return len(nums)
    
    def removeDuplicates(self, nums):
        nums[::] = [nums[x] for x in xrange(len(nums)) if nums[x] != nums[x-1] or x == 0]
        return len(nums)
