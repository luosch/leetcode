class Solution(object):
    def containsNearbyDuplicate_slow(self, nums, k):
        dic = dict()
        for i in range(len(nums)):
            if nums[i] in dic:
                if i - dic[nums[i]] <= k:
                    return True
                else:
                    dic[nums[i]] = i
            else:
                dic[nums[i]] = i

        return False
    
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False
