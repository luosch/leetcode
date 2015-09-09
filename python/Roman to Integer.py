class Solution(object):
    def romanToInt(self, s):
        ROMAN_MAP = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        total = 0
        prev = 0
        for i in range(len(s)):
            curr = ROMAN_MAP[s[i]]
            if curr > prev:
                total += curr - 2 * prev
            else:
                total += curr
            prev = curr
        return total
