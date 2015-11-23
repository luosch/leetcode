class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        start, end = 0, len(s) - 1
        while start < end:
            if not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -= 1
            else:
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else:
                    return False
        return True
