class Solution(object):
    def multiply(self, num1, num2):
        if num1 == 0 or num2 == 0:
            return 0
        len1, len2 = len(num1), len(num2)
        num = [0] * (len1 + len2)
        
        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                num[i + j + 1] += int(num1[i]) * int(num2[j])
        
        carry = 0
        for i in range(len1 + len2 - 1, -1, -1):
            tmp = num[i] + carry
            if tmp >= 10:
                carry = tmp // 10
                num[i] = tmp % 10
            else:
                carry = 0
                num[i] = tmp
                
        return .join(map(lambda x:str(x), num)).lstrip(0)

