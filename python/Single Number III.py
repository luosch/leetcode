class Solution(object):
    def singleNumber(self, nums):
        xor = 0
        for num in nums: xor ^= num
        xor = xor & (xor - 1) ^ xor
        a = b = 0
        for num in nums:
            if xor & num:
                a ^= num
            else:
                b ^= num
        return [a, b]
        
