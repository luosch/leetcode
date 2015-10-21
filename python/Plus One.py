class Solution(object):
    def plusOne(self, digits):
        ans = []
        digits[-1] += 1
        for i in range(len(digits) - 1, 0, -1):
            tmp = digits[i]
            if tmp >= 10:
                digits[i - 1] += 1
                tmp %= 10
            ans.append(tmp)
        
        num = digits[0]
        if num >= 10:
            num %= 10
            ans.append(num)
            ans.append(1)
        else:
            ans.append(num)
        
        return ans[::-1]
