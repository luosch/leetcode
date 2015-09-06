class Solution(object):
    def hammingWeight(self, n):
        sum = 0
        while n > 0:
            if n & 1:
                sum += 1 
            n >>= 1
        return sum
