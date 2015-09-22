class Solution(object):
    def singleNumber(self, nums):
        answer = 0
        single = [0 for x in range(32)]
        for num in nums:
            for i in xrange(32):
                if (num & (1 << i)):
                    single[i] = (single[i] + 1) % 3
        
        for i in range(0, 32):
            if i == 31 and single[i]:
                answer = -((1 << 31) - answer)
            else:
                answer |= single[i] * (1 << i)
        return answer
