class Solution(object):
    def majorityElement(self, nums):
        vote1, vote2 = 0, 0
        number1, number2 = 0, 0

        for num in nums:
            if number1 == num:
                vote1 += 1
            elif number2 == num:
                vote2 += 1
            elif vote1 == 0:
                number1 = num
                vote1 += 1
            elif vote2 == 0:
                number2 = num
                vote2 += 1
            else:
                vote1 -= 1
                vote2 -= 1
        
        count1, count2 = 0, 0
        ans = []
        for num in nums:
            if num == number1:
                count1 += 1
            elif num == number2:
                count2 += 1
        if count1 > len(nums) / 3:
            ans.append(number1)
        if count2 > len(nums) / 3:
            ans.append(number2)
        
        return ans
