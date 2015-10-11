class Solution(object):
    def reverseBits(self, n):
        answer = 0
        for i in range(32):
            answer = (answer << 1) + (n & 1)
            n >>= 1
        return answer
