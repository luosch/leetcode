class Solution(object):
    def majorityElement(self, nums):
        votes = 0
        number = 0
        for num in nums:
            if number == num:
                votes += 1
            elif votes == 0:
                number = num
                votes += 1
            else:
                votes -= 1
        return number
