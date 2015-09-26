class Solution(object):
    def convertToTitle(self, n):
        answer = ""
        base = ord(A)
        while n > 0:
            answer += chr(base + (n - 1) % 26)
            n -= ((n - 1) % 26 + 1)
            n /= 26

        return answer[::-1]
