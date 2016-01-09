class Solution(object):
    def lengthOfLongestSubstring(self, s):
        pos = [-1] * 256
        max_len = 0
        start = 0
        
        for i, c in enumerate(s):
            v = ord(c)
            if pos[v] == -1 or pos[v] < start:
                pos[v] = i
            else:
                if max_len < i - start:
                    max_len = i - start
                start = pos[v] + 1
                pos[v] = i
        
        return max(max_len, len(s) - start)
