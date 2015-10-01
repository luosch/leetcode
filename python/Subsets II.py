class Solution(object):
    def subsetsWithDup(self, nums):
        res = [[]]
        nums.sort()
        for num in nums: 
            res.extend([i + [num] for i in res if i + [num] not in res])
        return res
