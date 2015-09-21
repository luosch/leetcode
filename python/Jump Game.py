class Solution(object):
    def canJump(self, nums):
        max_reach = 0
        cursor = 0
        while cursor <= max_reach and cursor < len(nums):
            max_reach = max(max_reach, nums[cursor] + cursor)
            cursor += 1
        
        if max_reach >= len(nums) - 1:
            return True
        else:
            return False
