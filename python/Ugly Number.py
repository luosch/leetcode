class Solution(object):
    def isUgly(self, num):
        while num % 2 == 0 and num > 1: num /= 2
        while num % 3 == 0 and num > 1: num /= 3
        while num % 5 == 0 and num > 1: num /= 5
        return num == 1
