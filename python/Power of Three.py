class Solution(object):
    def isPowerOfThree(self, n):
        return n > 0 and 3 ** 19 % n == 0
    
    def isPowerOfThree_other(self, n):
        import math
        return n > 0 and 3 ** int(math.ceil(math.log(n, 3))) == n
