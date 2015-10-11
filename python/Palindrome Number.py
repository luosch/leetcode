class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        n, m = 1, 1
        while x // n:
            n *= 10
        
        n //= 10

        while n >= m:
            if x // n % 10 != x // m % 10:
                return False
            n //= 10
            m *= 10
        
        return True
