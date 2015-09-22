class Solution(object):
    def jump(self, nums):
        step, max_reach, cursor, last_reach = 0, 0, 0, -1
        
        while cursor <= max_reach and max_reach < len(nums) - 1:
            if max_reach < cursor + nums[cursor]:
                if last_reach < cursor:
                    step += 1
                    last_reach = max_reach
                
                max_reach = cursor + nums[cursor]
            cursor += 1
        
        return step
