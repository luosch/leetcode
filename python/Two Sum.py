class Solution(object):
    def twoSum(self, nums, target):
        nums_dict = dict()
        for i, v in enumerate(nums):
            if v not in nums_dict:
                nums_dict[v] = i
            if target - v in nums_dict:
                k = nums_dict[target - v]
                if k < i:
                    return [k + 1, i + 1]
