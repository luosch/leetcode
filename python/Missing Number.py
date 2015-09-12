class Solution(object):
    def missingNumber(self, nums):
        base = [False] * (len(nums) + 1)

        for num in nums:
            base[num] = True
        
        for i in range(len(base)):
            if base[i] == False:
                return i
