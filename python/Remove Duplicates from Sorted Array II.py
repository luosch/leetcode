class Solution(object):
    def removeDuplicates(self, nums):
        cursor1, cursor2, nums_len = 0, 2, len(nums)
        
        while cursor2 < nums_len:
            while nums[cursor1] == nums[cursor2]:
                nums.pop(cursor2)
                nums_len -= 1
                if cursor2 >= nums_len:
                    break
            
            cursor1 += 1
            cursor2 = cursor1 + 2
        
        return nums_len
