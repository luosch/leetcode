class Solution(object):
    def simplifyPath(self, path):
        stack = []
        for item in path.split(/):
            if not item in [., .., ]:
                stack.append(item)
            if item == .. and stack:
                stack.pop()
        
        return / + /.join(stack)
