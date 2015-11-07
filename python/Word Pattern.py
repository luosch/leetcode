class Solution(object):
    def wordPattern(self, pattern, str):
        str_list = str.split(' ')
        if len(pattern) != len(str_list):
            return False
        
        match = dict()
        for i in xrange(len(pattern)):
            if pattern[i] not in match:
                if str_list[i] not in match.values():
                    match[pattern[i]] = str_list[i]
                else:
                    return False
            else:
                if match[pattern[i]] != str_list[i]:
                    return False
            
        return True
