class Solution(object):
    def containsDuplicate(self, nums):
        dic = dict()
        for num in nums:
            if dic.get(num):
                return True
            dic[num] = True
        return False
