class Solution(object):
    def verifyPreorder(self, preorder):
        stack, low = [], float('-inf')
        for val in preorder:
            if val < low:
                return False
            while stack and stack[-1] < val:
                low = stack.pop()
            stack.append(val)
        
        return True
