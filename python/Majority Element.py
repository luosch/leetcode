class Solution(object):
    def majorityElement(self, nums):
        votes = 0
        number = 0
        for num in nums:
            if votes == 0:
                number = num
                votes += 1
            else:
                if number == num:
                    votes += 1
                else:
                    votes -= 1
        return number
        
