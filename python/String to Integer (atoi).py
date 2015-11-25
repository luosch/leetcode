class Solution(object):
    def myAtoi(self, str):
        isNegative = isBegin = False
        num, maxInt, minInt = 0, (1 << 31) - 1, -2147483648
        for c in str:
            if c == '-' and not isBegin:
                isNegative = True
                isBegin = True
            elif c == '+' and not isBegin:
                isBegin = True
            elif c.isdigit():
                isBegin = True
                num = num * 10 + ord(c) - ord('0')
                if isNegative and -num < minInt:
                    return minInt
                if not isNegative and num > maxInt:
                    return maxInt
            elif not isBegin and c == ' ':
                continue
            elif isBegin and not c.isdigit():    
                return -num if isNegative else num
            else:
                return 0
        return -num if isNegative else num
