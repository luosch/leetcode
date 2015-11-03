class Solution(object):
    def numOfBit(self, x):
        num_of_bit = 0
        while x > 0:
            x >>= 1
            num_of_bit += 1
        return num_of_bit

    def rangeBitwiseAnd(self, m, n):
        if m == n:
            return m
        
        num_m = self.numOfBit(m)
        num_n = self.numOfBit(n)
        
        if num_m != num_n:
            return 0
        
        num_diff = self.numOfBit(n - m)
        
        return m & n & (0xffffffff << num_diff)
    
    def rangeBitwiseAnd_slow(self, m, n):
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        
        return n << i
