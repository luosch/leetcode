class Solution(object):
    def longestPalindrome(self, s):
        # Manncher
        ss = '^#%s#$' % '#'.join(s)
        str_len = len(ss)
        p = [0] * str_len
        
        mx = idx = ans_len = ans_center = 0
        for i in range(1, str_len - 1):
            p[i] = min(p[2 * idx - i], mx - i) if mx > i else 1
            while ss[i + p[i]] == ss[i - p[i]]:
                p[i] += 1
            
            if i + p[i] > mx:
                mx = i + p[i]
                idx = i
            
            if p[i] > ans_len:
                ans_len = p[i]
                ans_center = i
        
        return s[(ans_center - ans_len) // 2:(ans_center + ans_len) // 2 - 1]
