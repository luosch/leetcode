class Solution(object):
    def isValid(self, s):
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if not top + c in ['()', '{}', '[]']:
                    return False
        
        if stack:
            return False
        else:
            return True
