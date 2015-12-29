class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        op = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '/': lambda x, y: x / y,
            '*': lambda x, y: x * y
        }
        for token in tokens:
            if token in op:
                stack[-2] = int(op[token](stack[-2], stack[-1]))
                stack.pop()
            else:
                stack.append(float(token))
        
        return int(stack[0])
