class Solution(object):
    def removeElement(self, nums, val):
        for num in nums[:]:
            if num == val:
                nums.remove(num)
        
        return len(nums)
