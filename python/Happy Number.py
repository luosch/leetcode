class Solution(object):
    def isHappy(self, n):
        tmp = n
        while tmp >= 10:
            tmp = 0
            while n:
                tmp += (n % 10) ** 2
                n //= 10
            n = tmp
        
        return tmp == 1 or tmp == 7
