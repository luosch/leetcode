class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return 
        
        min_len = len(strs[0])
        for s in strs:
            min_len = min(min_len, len(s))
        
        ans = 
        for i in range(min_len):
            c = strs[0][i]
            for s in strs:
                if s[i] != c:
                    return ans
            ans += c
        
        return ans
