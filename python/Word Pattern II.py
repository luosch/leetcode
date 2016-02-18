class Solution(object):
    def wordPatternMatch(self, pattern, str):
        self.dict = dict()
        return self.helper(pattern, str)
    
    def helper(self, pattern, str):
        if len(pattern) == 0 and len(str) > 0:
            return False
        if len(pattern) == 0 and len(str) == 0:
            return True
        
        for end in range(1, len(str) - len(pattern) + 2):
            if pattern[0] not in self.dict and str[:end] not in self.dict.values():
                self.dict[pattern[0]] = str[:end]
                if self.helper(pattern[1:], str[end:]):
                    return True
                del self.dict[pattern[0]]
            elif pattern[0] in self.dict and self.dict[pattern[0]] == str[:end]:
                if self.helper(pattern[1:], str[end:]):
                    return True
        
        return False
